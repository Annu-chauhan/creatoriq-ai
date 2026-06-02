from fastapi import APIRouter

from app.models.compare import CompareRequest

from app.services.transcript_service import (
    extract_transcript
)

from app.services.llm_service import (
    compare_creators
)

from app.services.youtube_metadata_service import (
    get_video_metadata
)

from app.services.engagement_service import (
    calculate_engagement_rate
)

router = APIRouter()


@router.post("/compare-videos")
async def compare_videos(
    request: CompareRequest
):

    video_a = extract_transcript(
        request.video_a
    )

    if "error" in video_a:
        return {
            "error": f"Video A: {video_a['error']}"
        }

    video_b = extract_transcript(
        request.video_b
    )

    if "error" in video_b:
        return {
            "error": f"Video B: {video_b['error']}"
        }

    metadata_a = get_video_metadata(
        request.video_a
    )

    metadata_b = get_video_metadata(
        request.video_b
    )

    engagement_a = calculate_engagement_rate(
        metadata_a["views"],
        metadata_a["likes"],
        metadata_a["comments"]
    )

    engagement_b = calculate_engagement_rate(
        metadata_b["views"],
        metadata_b["likes"],
        metadata_b["comments"]
    )
    print("VIDEO A LENGTH:", len(video_a["transcript"]))
    print("VIDEO B LENGTH:", len(video_b["transcript"]))

    result = compare_creators(
        video_a["transcript"],
        video_b["transcript"]
    )
    print("COMPARE RESULT:", result)
    return {
        "video_a": {
            **metadata_a,
            "engagement_rate": engagement_a
        },
        "video_b": {
            **metadata_b,
            "engagement_rate": engagement_b
        },
        "comparison": result["comparison"]
    }