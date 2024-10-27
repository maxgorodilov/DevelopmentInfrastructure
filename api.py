from fastapi import FastAPI, HTTPException
from task import router as user_router, users  # Импортируем хранилище пользователей

app = FastAPI()
@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}
@app.get("/users/{email}")
async def get_user(email: str):
    user = users.get(email)  # Доступ к хранилищу пользователей
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

app.include_router(user_router)






