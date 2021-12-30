# FastApi
from fastapi import FastAPI
from routes import user_routes, message_routes

app = FastAPI()

# Path Operations
app.include_router(user_routes.user)
app.include_router(message_routes.message)
