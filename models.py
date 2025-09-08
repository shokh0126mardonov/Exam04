from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String
)
from database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    
    user_id = Column('id', Integer, primary_key=True, index=True)
    user_name = Column("name", String(64), nullable=False)
    user_email = Column("email", String, nullable=False)

    tasks = relationship("Task", back_populates="user")


class Task(Base):
    __tablename__ = 'task'
    
    task_id = Column('id', Integer, primary_key=True, index=True)
    task_title = Column('title', String, nullable=False)
    task_status = Column('status', String, nullable=False)
    
    user_id = Column('user_id', Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="tasks")
