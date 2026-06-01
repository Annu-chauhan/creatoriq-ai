from fastapi import APIRouter

from app.models.video import VideoRequest

from app.services.transcript_service import (
    extract_transcript
)

from app.services.dashboard_service import (
    generate_dashboard
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

    dashboard = generate_dashboard(
        transcript_data["transcript"]
    )

    return {
        "video_id": transcript_data["video_id"],
        **dashboard
    }