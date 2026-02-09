from sqlalchemy.orm import Session
from model.task import Task
from schema.task_schema import TaskCreate


class TaskRepository:

    def create(self, db: Session, task: TaskCreate) -> Task:
        task = Task(**task.model_dump())
        db.add(task)
        db.commit()
        db.refresh(task)
        return task

    def find_all(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(Task).offset(skip).limit(limit).all()

    def find_by_id(self, db: Session, task_id: int):
        return db.query(Task).filter(Task.id == task_id).first()

    def update_task(self, db: Session, task: Task, task_name: str):
        task.task_name = task_name
        db.commit()
        db.refresh(task)
        return task

    def delete_task(self, db: Session, task_id: int):
        task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            return None
        db.delete(task)
        db.commit()
        return task
