from pydantic import BaseModel

class ComparisonRequest(BaseModel):

    youtube_url: str

    instagram_url: str