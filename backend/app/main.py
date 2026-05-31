from fastapi import FastAPI
from app.api.video import router as video_router

app = FastAPI(
    title="CreatorIQ AI",
    version="1.0.0"
)

app.include_router(video_router)

@app.get("/")
async def root():
    return {
        "status": "running",
        "project": "CreatorIQ AI"
    }