from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from celery.result import AsyncResult
from celery_app import (
    calcular_soma,
    calcular_fatorial,
    app as celery_app
)

app = FastAPI(
    title="API de Cálculos Realizados de Forma Assíncrona"
)

class RequisicaoSoma(BaseModel):
    a: float
    b: float

class RequisicaoFatorial(BaseModel):
    numero: int

@app.post("/soma")
def executar_soma(dados: RequisicaoSoma):
    tarefa = calcular_soma.delay(
        dados.a,
        dados.b
    )

    return {
        "mensagem": "Tarefa enviada com sucesso.",
        "task_id": tarefa.id
    }

@app.post("/fatorial")
def executar_fatorial(dados: RequisicaoFatorial):
    tarefa = calcular_fatorial.delay(
        dados.numero
    )

    return {
        "mensagem": "Tarefa enviada com sucesso.",
        "task_id": tarefa.id
    }

@app.get("/tarefas/{task_id}")
def consultar_tarefa(task_id: str):

    tarefa = AsyncResult(
        task_id,
        app=celery_app
    )

    if tarefa.state == "PENDING":
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada ou ainda não registrada."
        )

    resposta = {
        "task_id": task_id,
        "status": tarefa.state,
    }

    if tarefa.successful():
        resposta["resultado"] = tarefa.result

    if tarefa.failed():
        resposta["erro"] = str(tarefa.result)

    return resposta