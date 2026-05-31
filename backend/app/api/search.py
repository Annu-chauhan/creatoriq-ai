from fastapi import APIRouter

from app.models.search import SearchRequest
from app.services.embedding_service import create_embeddings
from app.services.qdrant_service import search_chunks

router = APIRouter()


@router.post("/search")
async def search(request: SearchRequest):

    query_embedding = create_embeddings(
        [request.question]
    )[0]

    results = search_chunks(query_embedding)

    return {
        "question": request.question,
        "results": results
    }