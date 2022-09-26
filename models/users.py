from asyncio import events
import imp
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event


class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]]


    class Config:
        schema_extra = {
            "example": {
                "email": "angelmoneze@gmail.com",
                "username": "strong...",
                "events": [],
            }
        }

class NewUser(User):
    pass 

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "angelmoneze@gmail.com",
                "password": "strong...",
                "events": [],
            }
        }