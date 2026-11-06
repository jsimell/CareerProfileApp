from uuid import uuid4

from fastapi import APIRouter

from app import database

router = APIRouter()

# User Creation Endpoint (only used when opening the app for the first time to create a user)


@router.post("/users", status_code=201)
def create_user():
    user_id = uuid4()
    database.create_user(user_id)
    return {"user_id": user_id}


@router.get("/users", status_code=200)  # For testing
def get_users():
    users = database.get_users()
    return users
