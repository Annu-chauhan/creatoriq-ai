from pydantic import BaseModel

class BrandMatchRequest(BaseModel):
    youtube_url: str
    brand_category: str