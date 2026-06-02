def generate_growth_audit(
    transcript,
    creator_analysis
):

    weaknesses = creator_analysis[
        "analysis"
    ]["weaknesses"]

    strengths = creator_analysis[
        "analysis"
    ]["strengths"]

    engagement_hooks = creator_analysis[
        "analysis"
    ]["engagement_hooks"]

    growth_score = 50

    growth_score += min(
        len(strengths) * 8,
        25
    )

    growth_score += min(
        len(engagement_hooks) * 5,
        15
    )

    growth_score -= min(
        len(weaknesses) * 5,
        20
    )

    growth_score = max(
        40,
        min(growth_score, 100)
    )

    opportunity_score = min(
        100,
        growth_score + 15
    )

    improvements = []

    if len(engagement_hooks) < 3:
        improvements.append(
            "Add stronger hooks"
        )

    if len(weaknesses) > 0:
        improvements.append(
            "Improve storytelling"
        )

    improvements.append(
        "Increase audience retention"
    )

    return {
        "growth_score": growth_score,
        "opportunity_score": opportunity_score,
        "weaknesses": weaknesses,
        "improvements": improvements
    }