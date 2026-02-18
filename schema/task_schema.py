from pydantic import BaseModel, ConfigDict

class TaskCreate(BaseModel):
    task_name: str

class TaskResponse(BaseModel):
    id: int
    task_name: str
    user_id: int

    class Config:
        model_config = ConfigDict(from_attributes=True)

class TaskUpdate(BaseModel):
    task_name: str

class TaskDelete(BaseModel):
    task_name: str

class MessageResponse(BaseModel):
    message: str
