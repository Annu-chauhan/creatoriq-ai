from fastapi import APIRouter
from app.models.video import VideoRequest
from app.services.transcript_service import extract_transcript
from app.services.strategy_service import generate_strategy

router = APIRouter()

@router.post("/content-strategy")
async def content_strategy(request: VideoRequest):

    transcript_data = extract_transcript(
        request.youtube_url
    )

    strategy = generate_strategy(
        transcript_data["transcript"]
    )

    return {
        "video_id": transcript_data["video_id"],
        "strategy": strategy
    }