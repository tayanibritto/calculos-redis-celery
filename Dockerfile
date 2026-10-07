FROM python:3.14-slim

WORKDIR /app

COPY pyproject.toml ./

RUN pip install poetry

COPY . .

RUN poetry config virtualenvs.create false && poetry install --no-root

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]