from fastapi import APIRouter,Depends
from src.task.task_model import CreateTaskRequestModel, TaskResponseModel,UpdateTaskRequestModel
from . import task_service
from typing import Annotated
from sqlalchemy.orm import Session
from src.config.database import get_db

task_router = APIRouter(prefix="/tasks",tags=["Task"])
database = Annotated[Session,Depends(get_db)]


@task_router.get("",response_model=TaskResponseModel)
def get_tasks(db:database):
    return task_service.get_tasks(db)

@task_router.get("/{id}",response_model=TaskResponseModel)
def get_task(id: int, db: database):
    return task_service.get_task(db,id)

@task_router.post("",response_model=TaskResponseModel)
def create_task(db:database,task_data:CreateTaskRequestModel):
    return task_service.create_task(db,task_data)

@task_router.patch("/{id}",response_model=TaskResponseModel)
def update_task(id: int, db: database, task_data: UpdateTaskRequestModel):
    return task_service.update_task(db,id, task_data)

@task_router.delete("/{id}",response_model=TaskResponseModel)
def delete_task(id: int, db: database):
    return task_service.delete_task(db,id) 