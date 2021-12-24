from typing import Optional
from pydantic import BaseModel

# Models


class Person(BaseModel):
    first_name: str
    last_name: str
    emil: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None
