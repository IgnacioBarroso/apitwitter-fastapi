#FastAPI
from fastapi import APIRouter, status, Body

#Models&Schemas
from models.tweet import Tweet
from schemas.tweet import tweetEntity, tweetsEntity

#MongoDB
from config.db import db
from bson.objectid import ObjectId

#Router
tweets_router = APIRouter(prefix="/tweets", tags=["Tweets"])


#Routes
@tweets_router.post("/post", status_code=status.HTTP_201_CREATED, summary="Post a tweet")
async def post_a_tweet(tweet: Tweet = Body(...)):
    db.tweets.insert_one(tweet.dict())
    return "Tweeted successfully" 

@tweets_router.get("/",status_code=status.HTTP_200_OK, summary="Show all tweets")
async def get_all_tweets():
    return tweetsEntity(db.tweets.find())

@tweets_router.get("/{tweet_id}", response_model=Tweet, status_code=status.HTTP_200_OK, summary="Get a tweet")
async def get_a_tweet(tweet_id: str):
    return tweetEntity(db.tweets.find_one({"_id": ObjectId(tweet_id)}))

@tweets_router.get("/{tweet_id}/delete", status_code=status.HTTP_200_OK, summary="Delete a tweet")
async def delete_a_tweet(tweet_id: str):
    tweet = db.tweets.find_one({"_id": ObjectId(tweet_id)})
    if tweet:
        db.tweets.delete_one({"_id": ObjectId(tweet_id)})
        return f"The {tweet_id} user has deleted", status.HTTP_200_OK
    return f"The {tweet_id} user does not exist", status.HTTP_404_NOT_FOUND

@tweets_router.get("/{tweet_id}/update", status_code=status.HTTP_200_OK, summary="Update a tweet")
async def update_a_tweet(tweet_id: str, tweet: Tweet = Body(...)):
    tweet_found = db.tweets.find_one({"_id": ObjectId(tweet_id)})
    if not tweet_found:
        return f"The user {tweet_id} does not exist", status.HTTP_404_NOT_FOUND
    db.tweets.update_one({"_id": ObjectId(tweet_id)}, {"$set": dict(tweet)})
    return f"The user {tweet_id} has updated"