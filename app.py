#Python
import json
from typing import Optional, List

#FastAPI
from fastapi import FastAPI, Body
from starlette import status

#Models
from tweets_routes import tweets_router
from users_routes import users_router

#App
app = FastAPI()

#Include the routers
app.include_router(tweets_router)
app.include_router(users_router)
