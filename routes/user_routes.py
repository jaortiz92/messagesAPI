# Python
from typing import List
from uuid import UUID, uuid1

# FastApi
from fastapi import APIRouter
from fastapi import status
from fastapi import Depends, HTTPException
from fastapi import Body, Path, Form
from pydantic.networks import EmailStr

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


def user_not_exist():
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="user_id does not exist"
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

    This path operation register an user in the app

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
    db_user = services.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    user.user_id = str(uuid1())

    return services.create_user(db, user)


@user.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
)
def login(
    email: EmailStr = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    """
    Login

    This path operation login an user in the app

    Parameters:
    - Request form parameters:
        - email: EmailStr
        - password: str

    Returns a json with the basic user information:
    - user_id: UUID
    - email: str
    - first_name: str
    - last_name: str
    - birth_date: str
    """
    response = services.get_user_by_email(db, email)
    if not response or response.password != password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email or password are not correct"
        )
    return response


@user.get(
    path="/",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all Users",
)
def show_all_users(db: Session = Depends(get_db)):
    """
    Show All Users

    This path operation show all users in the app

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
def show_a_user(
    user_id: UUID = Path(...),
    db: Session = Depends(get_db)
):
    """
    Show a user

    This path operation show an user in the app

    Parameters:
    - Register path parameter
        - user_id: UUID

    Returns a json with an users in the app, with the following keys
    - user_id: UUID
    - email: str
    - first_name: str
    - last_name: str
    - birth_date: str
    """
    response = services.get_user(db, str(user_id))
    if not response:
        user_not_exist()
    return response


@user.delete(
    path="/{user_id}/delete",
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
)
def delete_a_user(
    user_id: UUID = Path(...),
    db: Session = Depends(get_db)
):
    """
    Delete a User

    This path operation delete an user

    Parameters:
    - Register path parameter
        - user_id: UUID

    Return a json with information about deletion
    """
    response = services.delete_user(db, str(user_id))
    if not response:
        user_not_exist()
    return {"detail": response}


@user.put(
    path="/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User",
)
def update_a_user(
    user: User = Body(...),
    db: Session = Depends(get_db)
):
    """
    Update a User

    This path operation update an user

    Parameters
    - Register body parameter
        - user: User

    Returns a json with the basic user information:
    - user_id: UUID
    - email: str
    - first_name: str
    - last_name: str
    - birth_date: str
    """
    user.user_id = str(user.user_id)
    response = services.update_user(db, user)
    if not response:
        user_not_exist()
    return response
