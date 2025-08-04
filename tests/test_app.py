from fastapi.testclient import TestClient
from src.fastapi_zero.app import app
from http import HTTPStatus



def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app) # Arrange (organizacao)

    response = client.get('/') # Act (Acao) que executa o codigo

    assert response.status_code == HTTPStatus.OK # Assert (Asserto) afirmando que..., estagio final que queremos
    assert response.json() == {'message': 'Ola mundo'}  # Assert (Asserto) afirmando que exatamente isso.
