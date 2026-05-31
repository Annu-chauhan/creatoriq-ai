from pydantic import BaseModel

class VideoRequest(BaseModel):
    youtube_url: str
    instagram_url: str