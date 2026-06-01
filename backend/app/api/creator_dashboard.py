from fastapi import APIRouter

from app.models.video import VideoRequest

from app.services.transcript_service import (
    extract_transcript
)

from app.services.dashboard_service import (
    generate_dashboard
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

router = APIRouter()


@router.post("/creator-dashboard")
async def creator_dashboard(
    request: VideoRequest
):

    transcript_data = extract_transcript(
        request.youtube_url
    )

    print(transcript_data)

    if "error" in transcript_data:
        return {
            "video_id": transcript_data["video_id"],
            "error": transcript_data["error"]
        }

    transcript = transcript_data["transcript"]
    video_id = transcript_data["video_id"]

    # Store transcript in Qdrant
    create_collection()

    chunks = chunk_text(transcript)

    embeddings = create_embeddings(
        chunks
    )

    store_chunks(
        chunks,
        embeddings,
        video_id
    )

    dashboard = generate_dashboard(
        transcript
    )

    return {
        "video_id": video_id,
        **dashboard
    }