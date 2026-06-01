from fastapi import APIRouter

from app.models.brand_match import (
    BrandMatchRequest
)

from app.services.transcript_service import (
    extract_transcript
)

from app.services.llm_service import (
    analyze_creator
)

from app.services.brand_match_service import (
    calculate_brand_match
)

router = APIRouter()


@router.post("/brand-match")
async def brand_match(
    request: BrandMatchRequest
):

    transcript_data = extract_transcript(
        request.youtube_url
    )

    if "error" in transcript_data:
        return transcript_data

    creator_analysis = analyze_creator(
        transcript_data["transcript"]
    )

    result = calculate_brand_match(
        transcript_data["transcript"],
        creator_analysis,
        request.brand_category
    )

    return {
        "video_id": transcript_data["video_id"],
        **result
    }