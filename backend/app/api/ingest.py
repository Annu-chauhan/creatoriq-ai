from fastapi import APIRouter

from app.models.video import VideoRequest

from app.services.transcript_service import (
    extract_transcript
)

from app.services.chunking_service import (
    chunk_text
)

from app.services.embedding_service import (
    create_embeddings
)

from app.services.qdrant_service import (
    create_collection,
    store_chunks
)

from app.services.metadata_service import (
    get_video_metadata
)

router = APIRouter()


@router.post("/ingest-video")
async def ingest_video(
    request: VideoRequest
):

    youtube_data = extract_transcript(
        request.youtube_url,
        "youtube"
    )

    instagram_data = None

    if request.instagram_url:

        instagram_data = extract_transcript(
            request.instagram_url,
            "instagram"
        )

    transcript_data = youtube_data

    if "error" in transcript_data:

        return {
            "status": "error",
            "message": transcript_data["error"]
        }

    transcript = transcript_data["transcript"]

    video_id = transcript_data["video_id"]

    metadata = get_video_metadata(
        request.youtube_url
    )

    create_collection()

    chunks = chunk_text(
        transcript
    )

    embeddings = create_embeddings(
        chunks
    )

    total_chunks = store_chunks(
        chunks,
        embeddings,
        video_id,
        metadata
    )

    return {
        "status": "success",
        "video_id": video_id,
        "chunks_stored": total_chunks,
        "metadata": metadata,
        "instagram_processed": (
            instagram_data is not None
        )
    }