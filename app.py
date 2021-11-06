from fastapi import FastAPI

from tweets_routes import tweets_router
from users_routes import users_router

app = FastAPI()

app.include_router(tweets_router)
app.include_router(users_router)

@app.get("/", tags=["Home"])
def home():
    return {"message": "Hello World"}