from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel

from models import User
from database import user_utils

router = APIRouter(tags=["Users"])

@router.post("/users/", response_model=User)
async def create_user(request: Request, user: User):
    result = await user_utils.CreateNewUser(request.app.state.db, user)
    
    if result:
        raise HTTPException(
            status_code=400,
            detail="An account with the given username or email already exists!"
    )

    return user

@router.get("/users/{username}")
async def get_user(username: str):
    return username

@router.delete("/users/{username}")
async def delete_user(username: str):
    return "Deleted username!"

@router.put("/users/{username}", response_model=User)
async def update_user(user: User):
    return user
