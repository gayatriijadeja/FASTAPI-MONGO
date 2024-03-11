from fastapi import APIRouter

from models.ioc import PRL_db

from config.database import collection_name

from schema.schemas import list_serial

from bson import ObjectId

router = APIRouter()

#Get request method
@router.get("/")
async def get_iocs():
    iocs = list_serial(collection_name.find())
    return iocs     