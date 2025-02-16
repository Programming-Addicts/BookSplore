from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: Optional[int]
    first_name: Optional[str]
    last_name: Optional[str]
    discriminator: Optional[int]
    username: Optional[str]
    email: str
    avatar_url: Optional[str]
    followers: Optional[str]
    following: Optional[str]
    recent_books: Optional[str]
