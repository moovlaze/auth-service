from fastapi import FastAPI

import uvicorn

from src.apps.users import users_router
from src.core.helpers import init_db

app = FastAPI()
app.include_router(users_router)


if __name__ == "__main__":
    init_db()
    uvicorn.run(app="main:app", reload=True)
