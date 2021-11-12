#Python
from datetime import datetime
from typing import List

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
    new_tweet = {"content": tweet.content, "created_at": datetime.now(), "updated_at": datetime.now(), "user": tweet.user_id}
    result = db.execute(tweets_table.insert().values(new_tweet))
    return db.execute(tweets_table.select().where(tweets_table.c.id == result.lastrowid)).first()

@tweets_router.get("/",status_code=status.HTTP_200_OK, summary="Show all tweets")
async def get_all_tweets():
    return db.execute(tweets_table.select()).fetchall()

@tweets_router.get("/{tweet_id}", status_code=status.HTTP_200_OK, summary="Get a tweet")
async def get_tweet(tweet_id: int):
    return db.execute(tweets_table.select().where(tweets_table.c.id == tweet_id)).first()

@tweets_router.get("/{tweet_id}/delete", status_code=status.HTTP_200_OK, summary="Delete a tweet")
async def tweets_delete(tweet_id: int):
    db.execute(tweets_table.delete().where(tweets_table.c.id == tweet_id))
    return "Deleted"

@tweets_router.put("/{tweet_id}/update",status_code=status.HTTP_200_OK, summary="Update a tweet")
async def tweets_update(tweet_id: int, tweet: Tweet):
    updated_tweet = {"content": tweet.content, "updated_at": datetime.now()}
    db.execute(tweets_table.update().where(tweets_table.c.id == tweet_id).values(updated_tweet))
    return db.execute(tweets_table.select().where(tweets_table.c.id == tweet_id)).first()