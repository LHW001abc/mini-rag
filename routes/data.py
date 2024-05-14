from fastapi import FastAPI,UploadFile ,Depends ,  APIRouter

from helpers.config import get_settings ,Settings

from controller import DataConroller

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1" , "data"]
)

@data_router.post("/upload/{project_id}")

async def upload_data(project_id: str,file : UploadFile ,  app_settings: Settings =Depends(get_settings)):
   
    
    is_valid = DataConroller().validate_file(file)
   
    return is_valid


