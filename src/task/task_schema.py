from sqlalchemy import Column,Integer,String
from src.config.database import TableBase

class TaskSchema(TableBase):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True,autoincrement=True,index=True)
    name = Column(String(255),nullable=False,index=True)
    description = Column(String(255),nullable=True,index=True)