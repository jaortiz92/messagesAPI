from fastapi import FastAPI
from fastapi import Body
from models import Person

app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "World"}


@app.post("/person/new")
def create_person(person: Person = Body(...)):
    # (...) parameter need
    return person
