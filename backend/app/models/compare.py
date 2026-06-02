from pydantic import BaseModel


class CompareRequest(
    BaseModel
):

    video_a: str

    video_b: str