from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    

    response = client.get('/') # Act (Acao) que executa o codigo

    assert response.status_code == HTTPStatus.OK # Assert (Asserto) afirmando que..., estagio final que queremos
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert (Asserto) afirmando que exatamente isso.


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


def test_read_users(client):
    response = client.get('/users')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == { 'users': [
        {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
        }
    ]
    }



def test_update_user(client):
    response = client.put('/users/1', json={
            'password': '',
            'username': 'edson',
            'email': 'alice@example.com',
            'id': 1
        })

    assert response.json() == {
             
            'username': 'edson',
            'email': 'alice@example.com',
            'id': 1
        }
def test_not_found_update_user(client):
    response = client.put('users/5', json={'password': '',
            'username': 'edson',
            'email': 'alice@example.com',
            'id': 1})
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Usuário nao encontrado'}
    
def test_read_one_user(client):
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
            'username': 'edson',
            'email': 'alice@example.com',
            'id': 1
        }   

def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.json() == {'Message': 'Usuario deletado com sucesso!'}

def test_not_found_user(client):
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Usuário nao encontrado'}

