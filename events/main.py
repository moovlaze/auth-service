from fastapi import FastAPI

import uvicorn

from src.apps.users import users_router
from src.apps.admins import admins_router
from src.core.helpers import init_db


app = FastAPI()
app.include_router(users_router)
app.include_router(admins_router)

# TODO: сделать репозиторий для работы с БДшками и внедрение зависимостей для использования этого репозитория в контроллерах
# TODO: написать абстрактный класс для работы с брокерами

if __name__ == "__main__":
    init_db()
    uvicorn.run(app="main:app", reload=True)
