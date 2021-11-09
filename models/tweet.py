from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from .user import User

class Tweet(BaseModel):
    content: str = Field(...,min_length=1, max_length=140)
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=datetime.now())
    by: User = Field(...)