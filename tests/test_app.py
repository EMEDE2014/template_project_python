from http import HTTPStatus
from fastapi.testclient import TestClient
from fastapi_zero.app import app



def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app) # Arrange (organizacao)

    response = client.get('/') # Act (Acao) que executa o codigo

    assert response.status_code == HTTPStatus.OK # Assert (Asserto) afirmando que..., estagio final que queremos
    assert response.json() == {'message': 'Ola mundo'}  # Assert (Asserto) afirmando que exatamente isso.


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }