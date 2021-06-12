from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    hashed_password: str
