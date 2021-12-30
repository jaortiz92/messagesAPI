from fastapi import FastAPI
from models import User, UserLogin, Message


app = FastAPI()


@app.get(
    path="/"
)
def home():
    return {"Message API": "Working!!!"}
