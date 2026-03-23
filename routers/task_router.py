from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schema.task_schema import TaskUpdate, TaskCreate, MessageResponse, TaskResponse
from services.login_service import LoginService
from services.task_service import TaskService
from dependencies import get_db

router = APIRouter(prefix="/tasks", tags=["tasks"])
service = TaskService()
service_login = LoginService()

@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, user_id: int = Depends(service_login.verify_token), db: Session = Depends(get_db)):
    return service.create_task(db, task, user_id)


@router.get("/", response_model=list[TaskResponse])
def list_tasks(db: Session = Depends(get_db), user_id: int = Depends(service_login.verify_token)):
    return service.list_task(db, user_id)


@router.get("/{task_id}", response_model=TaskResponse)
def list_users_id(task_id: int, db: Session = Depends(get_db)):
    task = service.list_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/{task_id}", response_model=TaskResponse)
def update_user(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    return service.update_task(db, task_id, task)


@router.delete("/{task_id}", response_model=MessageResponse)
def delete_user(task_id: int, db: Session = Depends(get_db)):
    deleted = service.delete_task(db, task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": f"User {task_id} deleted"}
