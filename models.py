# Base
from uuid import UUID
from datetime import date, datetime
from typing import List, Optional

# Pydantic
from pydantic import BaseModel, EmailStr
from pydantic import Field


class BaseUser(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)


class User(BaseUser):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[date] = Field(
        default=None
    )


class UserLogin(BaseUser):
    password: str = Field(
        ...,
        min_length=8,
        max_length=256
    )


class Message(BaseModel):
    message_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
    )
    create_at: datetime = Field(
        default=datetime.now()
    )
    update_at: Optional[datetime] = Field(
        default=None
    )
    by: User = Field(...)
