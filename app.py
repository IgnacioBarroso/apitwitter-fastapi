#FastAPI
from fastapi import FastAPI

#Routes
from routes.tweets import tweets_router
from routes.users import users_router

#App
app = FastAPI()

#Include the routers
app.include_router(tweets_router)
app.include_router(users_router)
