import uvicorn
from fastapi import FastAPI
from database import Base, engine

from controller.task_controller import router as task_router
from controller.user_controller import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Project Task With FastAPI")

app.include_router(task_router)
app.include_router(user_router)

#if __name__ == '__main__':
    #uvicorn.run(app, host="127.0.0.1", port=8000)
