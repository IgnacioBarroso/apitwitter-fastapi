from cryptography.fernet import Fernet
#FastAPI
from fastapi import APIRouter, status

#Models
from config.db import db
from models.tables import users
from schemas.models import User

key = Fernet.generate_key()
f = Fernet(key)

#Router
users_router = APIRouter(prefix="/users", tags=["Users"])

#Auth routes
@users_router.post("/signup", status_code=status.HTTP_201_CREATED, summary="Register a user")
async def signup(user: User):
    new_user = {"name": user.first_name, "last_name": user.last_name, "email": user.email}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result = db.execute(users.insert().values(new_user))
    return db.execute(users.select().where(users.c.id == result.lastrowid)).first()

@users_router.post("/login", status_code=status.HTTP_200_OK, summary="Login a user")
async def login():
    pass

#User routes
@users_router.get("/", status_code=status.HTTP_200_OK, summary="Get all users")
async def get_all_users():
    return db.execute(users.select()).fetchall()

@users_router.get("/{user_id}", status_code=status.HTTP_200_OK, summary="Get a user")
async def get_user(user_id: str):
    return db.execute(users.select().where(users.c.id == user_id)).first()

@users_router.delete("/{user_id}/delete", status_code=status.HTTP_204_NO_CONTENT, summary="Delete a user")
async def delete_user(user_id: str):
    db.execute(users.delete().where(users.c.id == user_id))
    return "Deleted"

@users_router.put("/{user_id}/update", status_code=status.HTTP_200_OK, summary="Update a user")
async def update_user(user_id: str, user: User):
    db.execute(users.update().where(users.c.id == user_id).values(first_name = user.first_name, last_name = user.last_name, email = user.email, password = f.encrypt(user.password.encode("utf-8"))))
    return "Updated"