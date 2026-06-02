def calculate_engagement_rate(
    views,
    likes,
    comments
):

    if views == 0:
        return 0

    return round(
        (
            likes +
            comments
        )
        /
        views
        *
        100,
        2
    )
def calculate_engagement_rate(
    views,
    likes,
    comments
):

    if views == 0:
        return 0

    return round(
        (
            likes +
            comments
        )
        /
        views
        *
        100,
        2
    )