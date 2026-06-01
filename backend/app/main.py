from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.video import router as video_router
from app.api.vector import router as vector_router
from app.api.ingest import router as ingest_router
from app.api.search import router as search_router
from app.api.creator_analysis import router as creator_analysis_router
from app.api.content_strategy import router as content_strategy_router
from app.api.brand_match import router as brand_match_router
from app.api.growth_audit import router as growth_audit_router
from app.api.creator_dashboard import router as creator_dashboard_router
from app.api.chat import (router as chat_router)


app = FastAPI(
    title="CreatorIQ AI",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(video_router)
app.include_router(vector_router)
app.include_router(ingest_router)
app.include_router(search_router)
app.include_router(creator_analysis_router)
app.include_router(content_strategy_router)
app.include_router(brand_match_router)
app.include_router(growth_audit_router)
app.include_router(creator_dashboard_router)
app.include_router(chat_router)

@app.get("/")
async def root():
    return {
        "status": "running",
        "project": "CreatorIQ AI"
    }