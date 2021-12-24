from typing import Optional
from fastapi import FastAPI
from fastapi import Body, Query
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
    name: Optional[str] = Query(None, min_length=1, max_length=50),
    email: str = Query(..., regex=".+@.+\..+"),
    age: Optional[int] = Query(None, ge=18, le=100)
):
    return {"email": email,
            name: age}
