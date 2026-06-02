from fastapi import APIRouter

from app.models.video import VideoRequest

from app.services.transcript_service import (
    extract_transcript
)

from app.services.insights_service import (
    generate_insights
)

router = APIRouter()


@router.post("/video-insights")
async def video_insights(
    request: VideoRequest
):

    transcript_data = extract_transcript(
        request.youtube_url
    )

    if "error" in transcript_data:
        return {
            "error": transcript_data["error"]
        }

    return generate_insights(
        transcript_data["transcript"]
    )