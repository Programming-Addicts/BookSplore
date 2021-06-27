from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    session_id: Optional[str]
    id: Optional[int]
    first_name: str
    last_name: str
    email: str
    avatar_url: str
    followers: Optional[str]
    following: Optional[str]
