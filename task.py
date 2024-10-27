from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict

router = APIRouter()

# Хранилище пользователей
users: Dict[str, dict] = {}
class User(BaseModel):
    email: str
    full_name: str

@router.post("/users")
async def create_user(user: User) -> dict:
    if user.email in users:
        raise HTTPException(status_code=400, detail="Email already registered")
    users[user.email] = user.dict()
    return users[user.email]
