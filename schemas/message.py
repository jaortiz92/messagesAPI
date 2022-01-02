# Python
from uuid import UUID
from datetime import datetime
from typing import Optional

# Pydantic
from pydantic import BaseModel
from pydantic import Field

# Schemas
from .user import User


class BaseMessage(BaseModel):
    message_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
    )
    create_at: Optional[datetime] = Field(
        default=None
    )
    update_at: Optional[datetime] = Field(
        default=None
    )

    class Config:
        orm_mode = True


class Message(BaseMessage):
    user: User = Field(...)


class MessageCreate(BaseMessage):
    message_id: Optional[UUID] = Field(default=None)
    create_at: Optional[datetime] = Field(
        default=datetime.now()
    )
    user_id: UUID = Field(...)


class MessageUpdate(BaseMessage):
    update_at: Optional[datetime] = Field(
        default=datetime.now()
    )
