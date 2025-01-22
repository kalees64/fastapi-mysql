import dotenv
from fastapi import FastAPI
from src.task.task_router import task_router
from src.config.database import engine,TableBase

dotenv.load_dotenv()

app = FastAPI(title="FastAPI + MySQL",version="0.0.1")

@app.get("/",tags=["Default"])
def root():
    return {"data":"Welcome to FastAPI + MySQL API"}

app.include_router(task_router)

TableBase.metadata.create_all(bind=engine)