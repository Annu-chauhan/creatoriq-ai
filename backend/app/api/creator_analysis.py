from fastapi import APIRouter

from app.models.video import VideoRequest
from app.services.transcript_service import extract_transcript
from app.services.llm_service import analyze_creator

router = APIRouter()


@router.post("/creator-analysis")
async def creator_analysis(request: VideoRequest):

    transcript_data = extract_transcript(
        request.youtube_url
    )

    result = analyze_creator(
        transcript_data["transcript"]
    )

    return {
        "video_id": transcript_data["video_id"],
        **result
    }