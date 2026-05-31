from fastapi import FastAPI
from app.api.video import router as video_router
from app.api.vector import router as vector_router
from app.api.ingest import router as ingest_router
app = FastAPI(
    title="CreatorIQ AI",
    version="1.0.0"
)

app.include_router(video_router)
app.include_router(vector_router)
app.include_router(ingest_router)

@app.get("/")
async def root():
    return {
        "status": "running",
        "project": "CreatorIQ AI"
    }