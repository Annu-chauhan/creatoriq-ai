from youtube_transcript_api import (
    YouTubeTranscriptApi
)

from urllib.parse import (
    urlparse,
    parse_qs
)

import instaloader


def get_video_id(url):

    parsed = urlparse(url)

    return parse_qs(
        parsed.query
    )["v"][0]


def extract_youtube_transcript(url):

    video_id = get_video_id(url)

    try:

        ytt_api = YouTubeTranscriptApi()

        try:

            transcript = ytt_api.fetch(
                video_id,
                languages=["en"]
            )

        except:

            transcript = ytt_api.fetch(
                video_id,
                languages=["hi"]
            )

        full_text = " ".join(
            [
                snippet.text
                for snippet in transcript
            ]
        )

        return {
            "video_id": video_id,
            "platform": "youtube",
            "transcript": full_text
        }

    except Exception as e:

        return {
            "video_id": video_id,
            "error": str(e)
        }


def extract_instagram_transcript(url):

    try:

        shortcode = (
            url.split("/reel/")[1]
            .split("/")[0]
        )

        post = instaloader.Post.from_shortcode(
            instaloader.Instaloader().context,
            shortcode
        )

        return {
            "video_id": shortcode,
            "platform": "instagram",
            "transcript": post.caption or ""
        }

    except Exception as e:

        return {
            "video_id": "instagram",
            "error": str(e)
        }


def extract_transcript(
    url,
    platform="youtube"
):

    if platform == "instagram":

        return extract_instagram_transcript(
            url
        )

    return extract_youtube_transcript(
        url
    )