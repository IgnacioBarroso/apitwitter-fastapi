#Python
import json
from uuid import UUID
from datetime import date, datetime
from typing import Optional, List

#FastAPI
from fastapi import APIRouter, Body, status
from fastapi.param_functions import Form

#Pydantic
from pydantic import BaseModel, EmailStr, Field

#MongoDB
from config.db import db

#Router
users_router = APIRouter(prefix="/users", tags=["Users"])

#Models
class UserBase(BaseModel):
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(..., min_length=8, max_length=60)

class User(UserBase):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    birth_date: Optional[date] = Field(default=None)

class UserRegister(User):
    password: str = Field(..., min_length=8, max_length=60)

#Auth routes
@users_router.post("/signup", response_model=User, status_code=status.HTTP_201_CREATED, summary="Register a user")
async def signup(user: UserRegister = Form(...)):
    user = db.users.insert_one({
        "fist_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "birth_date": user.birth_date,
        "password": user.password,
    })
    return "The user has created"

@users_router.post("/login", response_model=User, status_code=status.HTTP_200_OK, summary="Login a user")
async def login():
    pass

#User routes
@users_router.get("/", response_model=List[User], status_code=status.HTTP_200_OK, summary="Get all users")
async def get_all_users():
    with open("users.json", "r", encoding="utf-8") as f:
        result = json.loads(f.read()) 
        return result

@users_router.get("/{user_id}", response_model=User, status_code=status.HTTP_200_OK, summary="Get a user")
async def get_user(user_id: int, user: User = Body(...)):
    return user

@users_router.delete("/{user_id}/delete", response_model=User, status_code=status.HTTP_200_OK, summary="Delete a user")
async def delete_user(user_id: int, user: User = Body(...)):
    return user

@users_router.put("/{user_id}/update", response_model=User, status_code=status.HTTP_200_OK, summary="Update a user")
async def update_user(user_id: int, user: User = Body(...)):
    return user