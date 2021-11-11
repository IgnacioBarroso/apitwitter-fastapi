#FastAPI
from fastapi import FastAPI

#Models
from routes.tweets_routes import tweets_router
from routes.users_routes import users_router

#App
app = FastAPI()

#Include the routers
app.include_router(tweets_router)
app.include_router(users_router)
