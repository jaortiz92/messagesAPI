# Python
from typing import List

# FastApi
from fastapi import APIRouter
from fastapi import status

# Schemas
from schemas import Message

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
def show_all_messages():
    return {"Message API": "Working!!!"}


@message.post(
    path="/post",
    response_model=Message,
    status_code=status.HTTP_201_CREATED,
    summary="Create a Message",
)
def create_a_message():
    pass


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
