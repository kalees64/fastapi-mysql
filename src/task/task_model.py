from pydantic import BaseModel
from typing import Optional,Union

class TaskModel(BaseModel):
    id:int
    name:str
    description:Union[str,None]
    
    class Config:
        orm_mode = True

class CreateTaskRequestModel(BaseModel):
    name:str
    description:Optional[str] = None
    
class UpdateTaskRequestModel(BaseModel):
    name:Optional[str] = None
    description:Optional[str] = None
    
class TaskResponseModel(BaseModel):
    data:TaskModel | list[TaskModel]