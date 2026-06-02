import yt_dlp


def get_video_metadata(url):

    ydl_opts = {
        "quiet": True
    }

    with yt_dlp.YoutubeDL(
        ydl_opts
    ) as ydl:

        info = ydl.extract_info(
            url,
            download=False
        )

        return {
            "title": info.get("title"),
            "creator": info.get("uploader"),

            "followers": info.get(
                "channel_follower_count"
            ) or 0,

            "views": info.get("view_count", 0),
            "likes": info.get("like_count", 0),
            "comments": info.get("comment_count", 0),
            "duration": info.get("duration"),
            "upload_date": info.get("upload_date"),
            "tags": info.get("tags", [])
        }