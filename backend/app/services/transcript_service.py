from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs


def get_video_id(url: str):
    parsed = urlparse(url)
    return parse_qs(parsed.query)["v"][0]


def extract_transcript(url: str):
    video_id = get_video_id(url)

    try:
        ytt_api = YouTubeTranscriptApi()

        # Try English first
        try:
            transcript = ytt_api.fetch(
                video_id,
                languages=["en"]
            )
        except:
            # Fallback to Hindi
            transcript = ytt_api.fetch(
                video_id,
                languages=["hi"]
            )

        full_text = " ".join(
            [snippet.text for snippet in transcript]
        )

        return {
            "video_id": video_id,
            "language": transcript.language,
            "transcript": full_text
        }

    except Exception as e:
        return {
            "video_id": video_id,
            "error": str(e)
        }