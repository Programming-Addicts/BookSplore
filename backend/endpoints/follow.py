from typing import List

from fastapi import APIRouter, Request

router = APIRouter(tags=["Follow Users"])

@router.post("/follow/{username}", response_model=str)
async def follow_user(request: Request, username: str):
    return f"Successfully followed {username}"

@router.get("/follow/{username}", response_model=List[str])
async def get_followers(request: Request, username: str):
    return ["User1", "User2", "User3"]

@router.delete("/follow/{username}", response_model=str)
async def unfollow_user(request: Request, username: str):
    return "Unfollowed user"
