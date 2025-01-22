from sqlalchemy.orm import Session
from src.task.task_model import CreateTaskRequestModel, TaskResponseModel, UpdateTaskRequestModel
from .task_schema import TaskSchema
from fastapi import HTTPException

def get_tasks(db:Session):
    tasks = db.query(TaskSchema).all()
    print(f'-- ALL Tasks : {tasks}')
    return {"data":tasks}

def get_task(db:Session,id:int):
    task = db.query(TaskSchema).filter(TaskSchema.id == id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"data":task}

def create_task(db:Session,task_data:CreateTaskRequestModel):
    new_task = TaskSchema(**task_data.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"data":new_task}

def update_task(db:Session,id:int,task_data:UpdateTaskRequestModel):
    update_task_data = task_data.model_dump(exclude_unset=True)
    if len(update_task_data.keys()) == 0:
        raise HTTPException(status_code=400, detail="No data to update")
    task = db.query(TaskSchema).filter(TaskSchema.id == id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    for key,value in update_task_data.items():
        setattr(task,key,value)
    db.commit()
    db.refresh(task)
    return {"data":task}

def delete_task(db:Session,id:int):
    task = db.query(TaskSchema).filter(TaskSchema.id == id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"data":task}