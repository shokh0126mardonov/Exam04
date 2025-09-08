from database import Base,engine,Session
from models import Task,User

Base.metadata.create_all(engine)