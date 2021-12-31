# Python
from typing import List

# FastApi
from fastapi import APIRouter
from fastapi import status
from fastapi import Depends, HTTPException
from fastapi import Body

# SQLalchemy
from sqlalchemy.orm import Session

# App
from schemas import User, UserRegister
from config import SessionLocal
import services

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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
def signup(
    user: UserRegister = Body(...),
    db: Session = Depends(get_db)
):
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
    db_user = services.user.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    user.user_id = str(user.user_id)

    return services.user.create_user(db, user)


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
def show_all_users(db: Session = Depends(get_db)):
    """
    Show All Users

    This path operation show all users  in the app

    Parameters:
    -

    Returns a json list with all users in the app, with the following keys
    - user_id: UUID
    - email: str
    - first_name: str
    - last_name: str
    - birth_date: str
    """
    return services.get_users(db, skip=0, limit=100)


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
