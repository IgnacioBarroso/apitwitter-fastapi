#Python
import json
from datetime import datetime, date
from uuid import UUID
from typing import Optional, List
from users_routes import User

#FastAPI
from fastapi import APIRouter, status, Body

#Pydantic
from pydantic import BaseModel, Field, EmailStr

#Router
tweets_router = APIRouter(prefix="/tweets", tags=["Tweets"])

#Model
class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(...,min_length=1, max_length=140)
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=datetime.now())
    by: User = Field(...)

#Routes
@tweets_router.post("/post", response_model=Tweet, status_code=status.HTTP_201_CREATED, summary="Post a tweet")
async def post_a_tweet(tweet: Tweet = Body(...)):
    with open("tweets.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        tweet_dict = tweet.dict()
        tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
        tweet_dict["content"] = str(tweet_dict["content"])
        tweet_dict["created_at"] = str(tweet_dict["created_at"])
        tweet_dict["updated_at"] = str(tweet_dict["updated_at"])
        tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"])
        tweet_dict["by"]["birth_date"] = str(tweet_dict["by"]["birth_date"])
        results.append(tweet_dict)
        f.seek(0)
        f.write(json.dumps(results, indent=4))
        return tweet

@tweets_router.get("/",response_model=List[Tweet],status_code=status.HTTP_200_OK, summary="Show all tweets")
async def get_all_tweets():
    with open("tweets.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        return results

@tweets_router.get("/{tweet_id}", response_model=Tweet, status_code=status.HTTP_200_OK, summary="Get a tweet")
async def tweets(tweet_id: int):
    return {"message": f"Tweet {tweet_id}"}

@tweets_router.get("/{tweet_id}/delete", response_model=Tweet, status_code=status.HTTP_200_OK, summary="Delete a tweet")
async def tweets_delete(tweet_id: int):
    return {"message": "Deleted Tweet {tweet_id}"}

@tweets_router.get("/{tweet_id}/update", response_model=Tweet, status_code=status.HTTP_200_OK, summary="Update a tweet")
async def tweets_update(tweet_id: int):
    return {"message": "Updated Tweet {tweet_id}"}