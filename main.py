from typing import Optional
from fastapi import FastAPI
from fastapi import Body, Query, Path
from pydantic.types import PositiveFloat
from models import Person, Location

app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "World"}


@app.post("/person/new")
def create_person(person: Person = Body(...)):
    # (...) parameter need
    return person


@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title="Person name",
        description="This is the person name. It's between 1 and 50 characers.",
        example="Juan"
    ),
    email: str = Query(
        ...,
        regex=".+@.+\..+",
        title="Person email",
        description="This is the email. It's required",
        example="juan@hotmail.com"
    ),
    age: Optional[int] = Query(
        None,
        ge=18,
        le=100,
        title="Person age",
        description="This is the person ege, It's between 18 and 100 years",
        example=26
    )
):
    return {"email": email,
            name: age}


@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="Person ID",
        description="This is the person ID. It's greater than 0. It's required.",
        example=12
    )
):
    return {person_id: "It exists!"}


@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="Person ID",
        description="This is the person ID. It's greater than 0. It's required.",
        example=12
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    results = person.dict()
    results.update(location.dict())
    return {person_id: results}
