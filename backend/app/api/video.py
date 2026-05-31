from fastapi import APIRouter

from app.models.video import VideoRequest
from app.services.metadata_service import extract_youtube_metadata

router = APIRouter()


@router.post("/youtube-metadata")
async def get_metadata(request: VideoRequest):

    metadata = extract_youtube_metadata(
        request.youtube_url
    )

    return metadata