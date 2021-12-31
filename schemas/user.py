# Python
from uuid import UUID
from datetime import date
from typing import Optional

# Pydantic
from pydantic import BaseModel, EmailStr
from pydantic import Field
from pydantic.fields import ModelField


class BaseUser(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

    class Config:
        orm_mode = True


class PasswordUser(BaseModel):
    password: str = Field(
        ...,
        min_length=8,
        max_length=256
    )


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


class UserLogin(PasswordUser, BaseUser):
    pass


class UserRegister(PasswordUser, User):
    pass
