#Python
from datetime import datetime

# FastAPI
from fastapi import APIRouter, status

#Models
from config.db import db
from models.tables import tweets_table
from schemas.models import Tweet

#Router
tweets_router = APIRouter(prefix="/tweets", tags=["Tweets"])

#Routes
@tweets_router.post("/post", status_code=status.HTTP_201_CREATED, summary="Post a tweet")
async def post_a_tweet(tweet: Tweet):
    new_tweet = {"content": tweet.content, "created_at": tweet.created_at, "updated_at": tweet.updated_at, "user_id": tweet.user_id}
    result = db.execute(tweets.insert().values(new_tweet))
    return db.execute(tweets.select().where(tweets.c.id == result.lastrowid)).first()

@tweets_router.get("/", status_code=status.HTTP_200_OK, summary="Show all tweets")
async def get_all_tweets():
    return db.execute(tweets_table.select()).fetchall()

@tweets_router.get("/{tweet_id}", status_code=status.HTTP_200_OK, summary="Get a tweet")
async def tweets(tweet_id: int):
    return db.execute(tweets.select().where(tweets.c.id == tweet_id)).first()

@tweets_router.get("/{tweet_id}/delete", status_code=status.HTTP_200_OK, summary="Delete a tweet")
async def tweets_delete(tweet_id: int):
    db.execute(tweets.delete().where(tweets.c.id == tweet_id))
    return "Deleted"

@tweets_router.get("/{tweet_id}/update", status_code=status.HTTP_200_OK, summary="Update a tweet")
async def tweets_update(tweet_id: int, user: Tweet):
    db.execute(tweets.update().where(tweets.c.id == tweet_id).values(content=user.content, updated_at=datetime.now()))
    return "Updated"