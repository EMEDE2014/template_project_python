from fastapi import FastAPI
from http import HTTPStatus


from fastapi_zero.schema import Message,UsersSchema ,UserPublic

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK ,response_model=Message)
def read_root():
    return {'message': 'Ola mundo'}
 


@app.post('users', status_code=HTTPStatus.CREATED,response_model=UserPublic)
def create_user(user: UsersSchema):

    return user

