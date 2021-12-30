# Python
from typing import List

# FastApi
from fastapi import FastAPI
from fastapi import status

# Models
from models import User, UserLogin, Message


app = FastAPI()

# Path Operations


@app.get(
    path="/"
)
def home():
    return {"Message API": "Working!!!"}

# Users


@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tag=["User"]
)
def signup():
    pass


@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tag=["User"]
)
def login():
    pass


@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all Users",
    tag=["User"]
)
def show_all_users():
    pass


@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tag=["User"]
)
def show_a_user():
    pass


@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tag=["User"]
)
def delete_a_user():
    pass


@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User",
    tag=["User"]
)
def update_a_user():
    pass
