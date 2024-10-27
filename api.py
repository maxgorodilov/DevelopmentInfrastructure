from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()
task_router = APIRouter()

users: Dict[str, dict] = {}

class User(BaseModel):
    email: str
    full_name: str

@task_router.post("/users")
async def create_user(user: User) -> dict:
    if user.email in users:
        raise HTTPException(status_code=400, detail="Email already registered")
    users[user.email] = user.dict()  # Исправлено здесь
    return users[user.email]

@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}

@app.get("/users/{email}")
async def get_user(email: str):
    user = users.get(email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

app.include_router(task_router)




