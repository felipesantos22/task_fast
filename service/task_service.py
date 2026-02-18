from sqlalchemy.orm import Session
from repositorie.task_repositorie import TaskRepository
from schema.task_schema import TaskCreate, TaskUpdate
from model.task import Task


class TaskService:

    def __init__(self):
        self.repository = TaskRepository()

    def create_task(self, db: Session, task_create: TaskCreate, user_id: int) -> Task:
        return self.repository.create(db, task_create, user_id)

    def list_task(self, db: Session, user_id: int):
        return self.repository.find_all_by_user(db, user_id)

    def list_task_by_id(self, db: Session, task_id: int):
        return self.repository.find_by_id(db, task_id)

    def update_task(self, db: Session, task_id: int, task_update: TaskUpdate):
        user = self.repository.find_by_id(db, task_id)
        return self.repository.update_task(db, user, task_update.task_name)

    def delete_task(self, db: Session, task_id: int):
        return self.repository.delete_task(db, task_id)
