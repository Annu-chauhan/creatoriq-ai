import yt_dlp


def get_instagram_metadata(url):

    try:

        ydl_opts = {
            "quiet": True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:

            info = ydl.extract_info(
                url,
                download=False
            )

            views = info.get("view_count", 0)
            likes = info.get("like_count", 0)
            comments = info.get("comment_count", 0)

            engagement_rate = (
                ((likes + comments) / views) * 100
                if views else 0
            )

            return {
                "platform": "instagram",
                "video_id": info.get("id"),
                "title": info.get("title"),
                "creator": info.get("uploader"),
                "followers": (
                 info.get("channel_follower_count")
                 or info.get("subscriber_count")
                 or 0
             ),
             
                "views": views,
                "likes": likes,
                "comments": comments,
                "duration": info.get("duration"),
                "upload_date": info.get("upload_date"),
                "engagement_rate": round(
                    engagement_rate,
                    2
                )
            }

    except Exception as e:

        print("INSTAGRAM ERROR:", e)

        return {}


def get_video_metadata(url):

    if "instagram.com" in url:
        return get_instagram_metadata(url)

    try:

        ydl_opts = {
            "quiet": True,
            "extract_flat": False
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:

            info = ydl.extract_info(
                url,
                download=False
            )

            views = info.get("view_count", 0)
            likes = info.get("like_count", 0)
            comments = info.get("comment_count", 0)

            engagement_rate = 0

            if views:
                engagement_rate = (
                    (likes + comments)
                    / views
                ) * 100

            return {
                "platform": "youtube",
                "video_id": info.get("id"),
                "title": info.get("title"),
                "creator": info.get("uploader"),
                "followers": info.get(
                 "channel_follower_count"
                ) or 0,
                "views": views,
                "likes": likes,
                "comments": comments,
                "duration": info.get("duration"),
                "upload_date": info.get("upload_date"),
                "hashtags": info.get("tags", []),
                "engagement_rate": round(
                    engagement_rate,
                    2
                )
            }

    except Exception as e:

        print("METADATA ERROR:", e)

        return {}