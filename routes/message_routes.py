# Python
from typing import List
from uuid import uuid1

# FastApi
from fastapi import APIRouter
from fastapi import status
from fastapi import Depends, HTTPException
from fastapi import Body
from sqlalchemy.orm.session import Session

# Schemas
from schemas import Message, MessageCreate
from config import SessionLocal
import services


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Message
message = APIRouter(
    prefix="/messages",
    tags=["Message"],
)


@message.get(
    path="/",
    response_model=List[Message],
    status_code=status.HTTP_200_OK,
    summary="Show all Messages",
)
def show_all_messages(
    db: Session = Depends(get_db)
):
    """
    Show All Messages

    This path operation show all messages in the app

    Parameters:
    -

    Returns a json list with all users in the app, with the following keys
    - message_id: UUID
    - content: str
    - create_at: datetame
    - update_at: datetame
    - user_id: str
    - user: str
    """
    return services.get_messages(db, 0, 100)


@message.post(
    path="/post",
    response_model=Message,
    status_code=status.HTTP_201_CREATED,
    summary="Create a Message",
)
def create_a_message(
    message: MessageCreate = Body(...),
    db: Session = Depends(get_db)
):
    """
    Create a Message

    This path operation register a message in the app

    Parameters:
    - Register body parameter
        - user: MessageCreate

    Returns a json with the basic message information:
    - message_id: UUID
    - content: str
    - create_at: datetame
    - update_at: datetame
    - user_id: str
    - user: str
    """

    message.message_id = str(uuid1())
    message.user_id = str(message.user_id)
    return services.message.create_message(db, message)


@message.get(
    path="/{message_id}",
    response_model=Message,
    status_code=status.HTTP_200_OK,
    summary="Show a Message",
)
def show_a_message():
    pass


@message.delete(
    path="/{mesage_id}/delete",
    response_model=Message,
    status_code=status.HTTP_200_OK,
    summary="Delete a Message",
)
def delete_a_message():
    pass


@message.put(
    path="/",
    response_model=Message,
    status_code=status.HTTP_200_OK,
    summary="Update all Messages",
)
def update_a_message():
    pass
