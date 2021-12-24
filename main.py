from typing import Optional
from fastapi import FastAPI
from fastapi import Body, Query, Path
from models import Person

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
        description="This is the person name. It's between 1 and 50 characers."
    ),
    email: str = Query(
        ...,
        regex=".+@.+\..+",
        title="Person email",
        description="This is the email. It's required"
    ),
    age: Optional[int] = Query(
        None,
        ge=18,
        le=100,
        title="Person age",
        description="This is the person ege, It's between 18 and 100 years"
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
        description="This is the person ID. It's greater than 0. It's required."
    )
):
    return {person_id: "It exists!"}
