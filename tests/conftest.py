# Os testes serao reconhecido se o nome do arquivo tiver nome de conftest.py ou iniciar com test_ ou terminar com _test.py
from fastapi.testclient import TestClient
import pytest
from fastapi_zero.app import app

# Fixture do pytest que cria um cliente de teste para a aplicação FastAPI, para que nao repita o codigo em todos os testes
@pytest.fixture()
def client():
    return TestClient(app)
