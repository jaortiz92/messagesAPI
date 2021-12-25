from typing import Optional
from pydantic import BaseModel

# Models


class Person(BaseModel):
    first_name: str
    last_name: str
    email: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


class Location(BaseModel):
    city: str
    state: str
    country: str
