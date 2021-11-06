from fastapi import APIRouter
from pydantic import BaseModel

tweets_router = APIRouter(prefix="/tweets", tags=["Tweets"])

class Tweet(BaseModel):
    id: int
    text: str
    user_id: int

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