from fastapi import APIRouter

from app.models.video import VideoRequest

from app.services.transcript_service import (
    extract_transcript
)

from app.services.growth_audit_service import (
    generate_growth_audit
)

router = APIRouter()


@router.post("/growth-audit")
async def growth_audit(
    request: VideoRequest
):

    transcript_data = extract_transcript(
        request.youtube_url
    )

    audit = generate_growth_audit(
        transcript_data["transcript"]
    )

    return {
        "video_id": transcript_data["video_id"],
        **audit
    }