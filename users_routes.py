#Python
from uuid import UUID
from datetime import date
from typing import Optional

#FastAPI
from fastapi import APIRouter, Body

#Pydantic
from pydantic import BaseModel, EmailStr, Field

#Router
users_router = APIRouter(prefix="/users", tags=["Users"])

#Models
class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(..., min_length=8)

class User(UserBase):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    birth_date: Optional[date] = Field(default=None)
    
#Routes
@users_router.post("/signup")
async def signup(user: User):
    return user

@users_router.post("/login")
async def login(user: User):
    return user

@users_router.get("/")
async def get_users(user: User = Body(...)):
    return user

@users_router.get("/{user_id}")
async def get_user(user_id: int, user: User = Body(...)):
    return user

@users_router.delete("/{user_id}/delete")
async def delete_user(user_id: int, user: User = Body(...)):
    return user

@users_router.put("/{user_id}/update")
async def update_user(user_id: int, user: User = Body(...)):
    return user