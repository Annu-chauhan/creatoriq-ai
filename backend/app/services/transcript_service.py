from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs


def get_video_id(url: str):
    parsed = urlparse(url)
    return parse_qs(parsed.query)["v"][0]


def extract_transcript(url: str):

    video_id = get_video_id(url)

    transcript = YouTubeTranscriptApi.get_transcript(
        video_id
    )

    full_text = " ".join(
        [item["text"] for item in transcript]
    )

    return {
        "video_id": video_id,
        "transcript": full_text
    }