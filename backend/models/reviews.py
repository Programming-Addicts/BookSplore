from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class Review(BaseModel):
    id: Optional[int]
    book_id: str
    user_id: int
    stay_anonymous: bool
    content: str
    timestamp: Optional[datetime]
    rating: int
