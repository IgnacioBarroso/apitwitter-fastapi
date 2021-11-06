#Python
import json
from uuid import UUID
from datetime import date
from typing import Optional, List

#FastAPI
from fastapi import APIRouter, Body, status

#Pydantic
from pydantic import BaseModel, EmailStr, Field

#Router
users_router = APIRouter(prefix="/users", tags=["Users"])

#Models
class UserBase(BaseModel):
    user_id: UUID = Field(...)
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
async def signup(user: UserRegister = Body(...)):
    with open("users.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results, indent=4))
        return user

@users_router.post("/login", response_model=User, status_code=status.HTTP_200_OK, summary="Login a user")
async def login():
    pass

#User routes
@users_router.get("/", response_model=List[User], status_code=status.HTTP_200_OK, summary="Get all users")
async def get_users():
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