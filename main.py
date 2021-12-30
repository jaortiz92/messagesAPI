# Python
from typing import List

# FastApi
from fastapi import FastAPI
from fastapi import status

# Models
from models import User, UserLogin, Message


app = FastAPI()

# Path Operations


# Users


@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["User"]
)
def signup():
    pass


@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["User"]
)
def login():
    pass


@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all Users",
    tags=["User"]
)
def show_all_users():
    pass


@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["User"]
)
def show_a_user():
    pass


@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["User"]
)
def delete_a_user():
    pass


@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User",
    tags=["User"]
)
def update_a_user():
    pass

# Message


@app.get(
    path="/",
    response_model=List[Message],
    status_code=status.HTTP_200_OK,
    summary="Show all Messages",
    tags=["Message"]

)
def show_all_messages():
    return {"Message API": "Working!!!"}


@app.post(
    path="/post",
    response_model=Message,
    status_code=status.HTTP_201_CREATED,
    summary="Create a Message",
    tags=["Message"]

)
def create_a_message():
    pass


@app.get(
    path="/messages/{message_id}",
    response_model=Message,
    status_code=status.HTTP_200_OK,
    summary="Show a Message",
    tags=["Message"]

)
def show_a_message():
    pass


@app.delete(
    path="/messages/{mesage_id}/delete",
    response_model=Message,
    status_code=status.HTTP_200_OK,
    summary="Delete a Message",
    tags=["Message"]

)
def delete_a_message():
    pass


@app.put(
    path="/",
    response_model=Message,
    status_code=status.HTTP_200_OK,
    summary="Update all Messages",
    tags=["Message"]

)
def update_a_message():
    pass
