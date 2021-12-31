# FastApi
from fastapi import FastAPI
from routes import user_routes, message_routes

# App
from config import SessionLocal, engine
from models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Path Operations
app.include_router(user_routes.user)
app.include_router(message_routes.message)
