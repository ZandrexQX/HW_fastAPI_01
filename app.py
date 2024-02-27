from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import logging
from HW_fastAPI_01.models import User

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
templates = Jinja2Templates(directory="./HW_fastAPI_01/templates")


users = []

for i in range(11):
    new_user = User(id=i, name=f"name_{i}", surname=f"surname_{i}", email=f"{i}@mail.ru",
                password=f"{5**2+2*i**3+7*(i+1)**2*100-i*25}")
    users.append(new_user)


@app.get('/')
async def root():
    logger.info('Отработал GET запрос')
    return {"Hello": "World"}


@app.get('/users/', response_class=HTMLResponse)
async def return_users(request: Request):
    logger.info('Отработал GET запрос для списка users')
    return templates.TemplateResponse("users.html", {'request': request, "users": users})


@app.get('/users/{user_id}')
async def read_user(user_id: int):
    logger.info(f'Отработал GET запрос для user id = {user_id}')
    return {'user_id': user_id}


@app.post('/users/')
async def create_user(user: User):
    logger.info('Отработал POST запрос')
    users.append(user)
    return user


@app.put('/users/{user_id}')
async def update_user(user_id: int, user: User):
    logger.info(f'Отработал PUT запрос для user id = {user_id}')
    for u in users:
        if u.id == user_id:
            u = user
            return {"user_id": user_id, "user": user}
    return {"message": f"user with {user_id} not found"}


@app.delete('/users/{user_id}')
async def delete_task(user_id: int):
    logger.info(f'Отработал DELETE запрос для user id = {user_id}')
    for u in users:
        if u.id == user_id:
            users.remove(u)
            return {"message": f"delete {user_id}"}
    return {"message": f"user with {user_id} not found"}
