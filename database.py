from sqlalchemy import(
    create_engine,
    URL,
    MetaData
)
from sqlalchemy.orm import sessionmaker

from config import DB_HOST,DB_NAME,DB_PASSWORD,DB_PORT,DB_USER
from sqlalchemy.ext.declarative import declarative_base

url_object = URL.create(
    "postgresql+psycopg2",  
    username=DB_USER,
    password=DB_PASSWORD,  
    host=DB_HOST,
    database=DB_NAME,
    port=DB_PORT
)

engine = create_engine(url_object)

Base = declarative_base()

Session = sessionmaker(autoflush=True,autocommit = False,bind=engine)