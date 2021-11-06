#Python
import json
from typing import Optional, List

#FastAPI
from fastapi import FastAPI, Body
from starlette import status

#Models
from tweets_routes import Tweet, tweets_router
from users_routes import User, users_router

app = FastAPI()

#Include the routers
app.include_router(tweets_router)
app.include_router(users_router)

#Home
@app.get("/",response_model=List[Tweet],status_code=status.HTTP_200_OK, summary="Show all tweets", tags=["Tweets"])
def home():
    with open("tweets.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        return results