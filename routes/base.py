from fastapi import FastAPI , APIRouter

import os
base_router = APIRouter(
    prefix="/api/v1"
)
@base_router.get("/")

async def welcome():
    name = os.getenv("APP_NAME")
    return {"message": "Welcome to the FastAPI" + name + " "}
