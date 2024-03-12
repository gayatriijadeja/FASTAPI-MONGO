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

#Post request method
@router.post("/")
async def post_iocs(ioc: str):
    collection_name.insert_one(dict(ioc))

#Put request method
@router.put("/{id}")
async def put_iocs( id : str, ioc : str):
    collection_name.find_one_and_update({"_id" : ObjectId (id)}, {"$set": dict(ioc)})

#Delete request method
@router.delete("\{id}")
async def delete_iocs(id: str):
    collection_name.find_one_and_delete({"_id" : ObjectId(id)})
