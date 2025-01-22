from sqlalchemy import create_engine
from dotenv import load_dotenv
from os import getenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


load_dotenv()

engine = create_engine(getenv("DATABASE_URI"))

session_local = sessionmaker(autocommit=False,autoflush=False,bind=engine)

TableBase = declarative_base()

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()