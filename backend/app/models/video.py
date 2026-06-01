from pydantic import BaseModel
from typing import Optional


class VideoRequest(BaseModel):
    youtube_url: str
    instagram_url: Optional[str] = None