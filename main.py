import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from database import Base, engine

from routers.task_router import router as task_router
from routers.user_router import router as user_router
from routers.login_router import router as login_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Project Task With FastAPI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task_router)
app.include_router(user_router)
app.include_router(login_router)

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
