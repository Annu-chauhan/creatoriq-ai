from fastapi import APIRouter

from app.models.video import VideoRequest
from app.services.transcript_service import extract_transcript
from app.services.chunking_service import chunk_text
from app.services.embedding_service import create_embeddings
from app.services.qdrant_service import (
    create_collection,
    store_chunks
)

router = APIRouter()


@router.post("/ingest-video")
async def ingest_video(request: VideoRequest):

    transcript_data = extract_transcript(
        request.youtube_url
    )

    transcript = transcript_data["transcript"]

    video_id = transcript_data["video_id"]

    create_collection()

    chunks = chunk_text(transcript)

    embeddings = create_embeddings(chunks)

    total_chunks = store_chunks(
        chunks,
        embeddings,
        video_id
    )

    return {
        "status": "success",
        "video_id": video_id,
        "chunks_stored": total_chunks
    }