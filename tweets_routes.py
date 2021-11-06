#Python
from datetime import datetime
from uuid import UUID
from typing import Optional
from users_routes import User

#FastAPI
from fastapi import APIRouter

#Pydantic
from pydantic import BaseModel, Field

#Router
tweets_router = APIRouter(prefix="/tweets", tags=["Tweets"])

#Model
class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(..., max_length=140)
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=datetime.now())
    by: User = Field(...)

#Routes
@tweets_router.get("/post")
async def post():
    return {"message": "Post"}

@tweets_router.get("/{tweet_id}")
async def tweets(tweet_id: int):
    return {"message": f"Tweet {tweet_id}"}

@tweets_router.get("/{tweet_id}/delete")
async def tweets_delete(tweet_id: int):

    return {"message": f"Deleted Tweet {tweet_id}"}
@tweets_router.get("/{tweet_id}/update")
async def tweets_update(tweet_id: int):
    return {"message": f"Updated Tweet {tweet_id}"}