from fastapi import FastAPI

import uvicorn

from src.apps.users import users_router

app = FastAPI()
app.include_router(users_router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
