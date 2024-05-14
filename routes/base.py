from fastapi import FastAPI ,Depends ,  APIRouter

from helpers.config import get_settings ,Settings

base_router = APIRouter(
    prefix="/api/v1"
)
@base_router.get("/")

async def welcome(app_settings: Settings =Depends(get_settings)):
  #  app_settings = get_settings()
    name = app_settings.APP_NAME
    version = app_settings.APP_VERSION
    return {"message": "Welcome to the FastAPI" + name + " " + version + " "}
 
