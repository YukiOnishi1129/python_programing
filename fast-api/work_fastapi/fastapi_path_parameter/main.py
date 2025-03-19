from fastapi import FastAPI, HTTPException
from typing import Optional
from data import get_user, User

app = FastAPI()

@app.get("/users/{user_id}")
async def read_user(user_id: int) -> dict:
    user: Optional[User] = get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user.id, "name": user.name}