from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    email: str
    avatar_url: str
    followers: Optional[str]
    following: Optional[str]