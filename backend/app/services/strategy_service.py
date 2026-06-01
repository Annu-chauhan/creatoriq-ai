def generate_strategy(
    transcript,
    creator_analysis
):

    niche = creator_analysis["analysis"][
        "content_niche"
    ]

    return {
        "content_ideas": [
            f"Top 5 {niche} Facts",
            f"Beginner Guide To {niche}",
            f"Common {niche} Mistakes"
        ],

        "viral_hooks": [
            f"Most people don't know this about {niche}",
            f"The biggest mistake in {niche}",
            f"This changes everything in {niche}"
        ],

        "growth_opportunities": [
            "Create Shorts",
            "Improve storytelling",
            "Add stronger hooks"
        ],

        "posting_strategy":
            "3 videos per week"
    }