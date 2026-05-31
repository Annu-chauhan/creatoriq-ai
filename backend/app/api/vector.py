from fastapi import APIRouter
from app.services.qdrant_service import create_collection

router = APIRouter()


@router.post("/create-vector-db")
async def create_vector_db():

    create_collection()

    return {
        "status": "success",
        "collection": "video_chunks"
    }