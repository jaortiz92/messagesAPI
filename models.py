from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum

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
    email: str = Field(
        ...,
        regex=".+@.+\..+",
    )
    age: int = Field(
        ...,
        ge=18,
        le=100,
    )
    hair_color: Optional[HairColor] = Field(
        default=None,
    )
    is_married: Optional[bool] = Field(
        default=None,
    )


class Location(BaseModel):
    city: str
    state: str
    country: str
