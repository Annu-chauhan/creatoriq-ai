from fastapi import APIRouter

from app.models.video import VideoRequest
from app.services.metadata_service import get_video_metadata
from app.services.transcript_service import extract_transcript

router = APIRouter()


@router.post("/youtube-metadata")
async def get_metadata(request: VideoRequest):

    metadata = get_video_metadata(
        request.youtube_url
    )

    return metadata


@router.post("/youtube-transcript")
async def get_transcript(request: VideoRequest):

    return extract_transcript(
        request.youtube_url
    )