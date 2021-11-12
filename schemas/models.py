from pydantic import BaseModel, Field
from pydantic.networks import EmailStr
from typing import Optional
from datetime import date

class Tweet(BaseModel):
    id: Optional[int]
    user_id: int
    content: str
    created_at: str
    updated_at: str
    

class UserBase(BaseModel):
    email: EmailStr = Field(...)

#class UserLogin(UserBase):
    #password: str = Field(..., min_length=8, max_length=60)

class User(UserBase):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    birth_date: Optional[date] = Field(default=None)

class UserRegister(User):
    password: str = Field(..., min_length=8, max_length=60)

class UserResponseID(User):
    id: int    