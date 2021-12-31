# Python
from typing import List

# FastApi
from fastapi import APIRouter
from fastapi import status

# Schemas
from schemas import User

# Users
user = APIRouter(
    prefix="/users",
    tags=["User"],
)


@user.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
)
def signup():
    """
    Signup

    This path operation register a user in the app

    Parameters:
    - Register body parameter
        - user: UserRegister

    Returns a json with the basic user information:
    - user_id: UUID
    - email: str
    - first_name: str
    - last_name: str
    - birth_date: str
    """
    pass


@user.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
)
def login():
    pass


@user.get(
    path="/",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all Users",
)
def show_all_users():
    pass


@user.get(
    path="/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
)
def show_a_user():
    pass


@user.delete(
    path="/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
)
def delete_a_user():
    pass


@user.put(
    path="/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User",
)
def update_a_user():
    pass
