from fastapi import FastAPI

from app.api.video import router as video_router
from app.api.vector import router as vector_router
from app.api.ingest import router as ingest_router
from app.api.search import router as search_router
from app.api.creator_analysis import (
    router as creator_analysis_router
)

app = FastAPI(
    title="CreatorIQ AI",
    version="1.0.0"
)

app.include_router(video_router)
app.include_router(vector_router)
app.include_router(ingest_router)
app.include_router(search_router)
app.include_router(creator_analysis_router)

@app.get("/")
async def root():
    return {
        "status": "running",
        "project": "CreatorIQ AI"
    }