# Python
from typing import List
from uuid import UUID, uuid1

# FastApi
from fastapi import APIRouter
from fastapi import status
from fastapi import Depends, HTTPException
from fastapi import Body
from fastapi.param_functions import Path
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


def message_not_exist():
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="message_id does not exist"
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
    - user: User
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
def show_a_message(
    message_id: UUID = Path(...),
    db: Session = Depends(get_db)
):
    """
    Show a message

    This path operation show a message in the app

    Parameters:
    - Register path parameter
        - message_id: UUID

    Returns a json with a message in the app, with the following keys
    - message_id: UUID
    - content: str
    - create_at: datetame
    - update_at: datetame
    - user: User
    """
    db_message = services.get_message(db, str(message_id))
    if not db_message:
        message_not_exist()
    return db_message


@message.delete(
    path="/{message_id}/delete",
    response_model=Message,
    status_code=status.HTTP_200_OK,
    summary="Delete a Message",
)
def delete_a_message():
    pass


@message.put(
    path="/update",
    response_model=Message,
    status_code=status.HTTP_200_OK,
    summary="Update all Messages",
)
def update_a_message():
    pass
