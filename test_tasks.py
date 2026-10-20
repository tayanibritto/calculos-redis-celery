from unittest.mock import patch
from celery_app import (
    calcular_soma,
    calcular_fatorial
)

@patch("celery_app.time.sleep")
def test_calcular_soma(mock_sleep):
    resultado = calcular_soma.run(3, 5)
    assert resultado == 8

@patch("celery_app.time.sleep")
def test_calcular_fatorial(mock_sleep):
    resultado = calcular_fatorial.run(5)
    assert resultado == 120

@patch("celery_app.time.sleep")
def test_calcular_fatorial_zero(mock_sleep):
    resultado = calcular_fatorial.run(0)
    assert resultado == 1