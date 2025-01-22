import dotenv
from fastapi import FastAPI

dotenv.load_dotenv()

app = FastAPI()

@app.get("/")
def root():
    return {"data":"Welcome to FastAPI + MySQL API"}