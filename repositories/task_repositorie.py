from sqlalchemy.orm import Session
from models.task import Task
from schema.task_schema import TaskCreate


class TaskRepository:

    def create(self, db: Session, task_create: TaskCreate, user_id: int) -> Task:
        task = Task(
            **task_create.model_dump(),
            user_id=user_id
        )
        db.add(task)
        db.commit()
        db.refresh(task)
        return task

    def find_all_by_user(self, db: Session, user_id: int):
        return db.query(Task).filter(Task.user_id == user_id).all()

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
