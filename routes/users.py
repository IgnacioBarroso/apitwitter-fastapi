#FastAPI
from fastapi import APIRouter, Body, status

#Models&Schemas
from models.user import User, UserRegister
from schemas.user import userEntity, usersEntity

#MongoDB
from config.db import db
from bson.objectid import ObjectId

#Router
users_router = APIRouter(prefix="/users", tags=["Users"])

#Auth routes
@users_router.post("/signup", status_code=status.HTTP_201_CREATED, summary="Register a user")
async def signup(user: UserRegister = Body(...)):
        db.users.insert_one(user.dict())
        return f"User {user.first_name} {user.last_name} created successfully" 

@users_router.post("/login", response_model=User, status_code=status.HTTP_200_OK, summary="Login a user", deprecated=True)
async def login():
    pass

#User routes
@users_router.get("/", status_code=status.HTTP_200_OK, summary="Get all users")
async def get_all_users():
    return usersEntity(db.users.find())
    
@users_router.get("/{user_id}", status_code=status.HTTP_200_OK, summary="Get a user")
async def get_user(user_id: str):
    return userEntity(db.users.find_one({"_id": ObjectId(user_id)}))

@users_router.delete("/{user_id}/delete", status_code=status.HTTP_200_OK, summary="Delete a user")
async def delete_user(user_id: str):
    user = db.users.find_one({"_id": ObjectId(user_id)})
    if user:
        db.users.delete_one({"_id": ObjectId(user_id)})
        return f"The {user_id} user has deleted", status.HTTP_200_OK
    return f"The {user_id} user does not exist", status.HTTP_404_NOT_FOUND

@users_router.put("/{user_id}/update", status_code=status.HTTP_200_OK, summary="Update a user")
async def update_user(user_id: str, user: User = Body(...)):
    user_found = db.users.find_one({"_id": ObjectId(user_id)})
    if not user_found:
        return f"The user {user_id} does not exist", status.HTTP_404_NOT_FOUND
    db.users.update_one({"_id": ObjectId(user_id)}, {"$set": dict(user)})
    return f"The user {user_id} has updated"