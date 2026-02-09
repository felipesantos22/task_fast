from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schema.task_schema import TaskUpdate, TaskCreate, TaskDelete, MessageResponse, TaskResponse
from service.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])
service = TaskService()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return service.create_task(db, task)


@router.get("/", response_model=list[TaskResponse])
def list_tasks(db: Session = Depends(get_db)):
    return service.repository.find_all(db)


@router.get("/{task_id}", response_model=TaskResponse)
def list_users_id(task_id: int, db: Session = Depends(get_db)):
    task = service.repository.find_by_id(db, task_id)
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
