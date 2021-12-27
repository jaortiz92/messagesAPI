# Python
from typing import Optional

# FastApi
from fastapi import FastAPI
from fastapi import Body, Query, Path, Form, Header, Cookie, UploadFile, File
from fastapi import status
from fastapi import HTTPException

# Pydantic
from pydantic.networks import EmailStr

# Models
from models import Person, Location, PersonOut, LoginOut


app = FastAPI()


@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    tags=["Others"]
)
def home():
    return {"Hello": "World"}


@app.post(
    path="/person/new",
    response_model=PersonOut,
    status_code=status.HTTP_201_CREATED,
    tags=["Person"]
)
def create_person(person: Person = Body(...)):
    # (...) parameter need
    return person


@app.get(
    path="/person/detail",
    status_code=status.HTTP_200_OK,
    tags=["Person"]
)
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


persons = [1, 2, 3, 4, 5]


@app.get(
    path="/person/detail/{person_id}",
    status_code=status.HTTP_200_OK,
    tags=["Person"]
)
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="Person ID",
        description="This is the person ID. It's greater than 0. It's required.",
        example=12
    )
):
    if person_id not in persons:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="¡This person doesn't exist!"
        )
    return {person_id: "It exists!"}


@app.put(
    path="/person/{person_id}",
    status_code=status.HTTP_200_OK,
    tags=["Person"]
)
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


@app.post(
    path="/login",
    response_model=LoginOut,
    status_code=status.HTTP_200_OK,
    tags=["Person"]
)
def login(username: str = Form(...), password: str = Form(...)):
    loginOut = LoginOut(username=username)
    return loginOut


@app.post(
    path="/contact",
    status_code=status.HTTP_200_OK,
    tags=["Others"]
)
def contact(
    first_name: str = Form(
        ...,
        max_length=20,
        min_length=1
    ),
    last_name: str = Form(
        ...,
        max_length=20,
        min_length=1
    ),
    email: EmailStr = Form(...),
    message: str = Form(
        ...,
        min_length=20
    ),
    user_agent: Optional[str] = Header(default=None),
    ads: Optional[str] = Cookie(default=None)
):
    return user_agent


@app.post(
    path="/post-image",
    tags=["Posts"]
)
def post_image(
    image: UploadFile = File(...)
):
    return {
        "Filename": image.filename,
        "Format": image.content_type,
        "Size(kb)": round(len(image.file.read())/1024, ndigits=2)
    }
