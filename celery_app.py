from celery import Celery
import time

app = Celery(
    "tarefas",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
)

app.conf.update(
    task_track_started=True
)

@app.task
def calcular_soma(a: float, b: float):
    print(f"Iniciando soma: {a} + {b}")

    time.sleep(5)

    resultado = a + b

    print(f"Resultado da soma: {resultado}")

    return resultado

@app.task
def calcular_fatorial(numero: int):
    print(f"Iniciando cálculo do fatorial de {numero}")

    if numero < 0:
        raise ValueError("Não existe fatorial de números negativos.")

    time.sleep(10)

    resultado = 1

    for i in range(2, numero + 1):
        resultado *= i

    print(f"Fatorial de {numero}: {resultado}")

    return resultado