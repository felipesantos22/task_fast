from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    user_name = Column(String(20),nullable=False)
    password = Column(String(250), nullable=False)
    tasks = relationship("Task", back_populates="user")