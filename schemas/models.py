from pydantic import BaseModel
from pydantic.networks import EmailStr
from typing import Optional

class User(BaseModel):
    id: Optional[int]
    email: EmailStr
    first_name: str
    last_name: str
    birth_date: str
    password: str

class Tweet(BaseModel):
    id: Optional[int]
    content: str
    created_at: str
    updated_at: str
    user_id: int

#class UserBase(BaseModel):
    #user_id: UUID = Field(...)
    #email: EmailStr = Field(...)

#class UserLogin(UserBase):
    #password: str = Field(..., min_length=8, max_length=60)

#class User(UserBase):
    #first_name: str = Field(..., min_length=1, max_length=50)
    #last_name: str = Field(..., min_length=1, max_length=50)
    #birth_date: Optional[date] = Field(default=None)

#class UserRegister(User):
    #password: str = Field(..., min_length=8, max_length=60)    