from typing import Optional
from pydantic import BaseModel, Field, HttpUrl, EmailStr

from enum import Enum
from datetime import date
from test_models import schema_person, schema_location

# Models


class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"


class Person(BaseModel):
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
    email: EmailStr = Field(
        ...,
    )
    age: int = Field(
        ...,
        ge=18,
        le=100,
    )
    website: Optional[HttpUrl] = Field(
        default=None
    )
    birth_date: Optional[date] = Field(
        default=None
    )
    hair_color: Optional[HairColor] = Field(
        default=None,
    )
    is_married: Optional[bool] = Field(
        default=None,
    )

    class Config:
        schema_extra = schema_person


class Location(BaseModel):
    city: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    state: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    country: str = Field(
        ...,
        min_length=1,
        max_length=50
    )

    class Config:
        schema_extra = schema_location
