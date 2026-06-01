def generate_growth_audit(
    transcript,
    creator_analysis
):

    weaknesses = creator_analysis[
        "analysis"
    ]["weaknesses"]

    improvements = [
        "Improve storytelling",
        "Add stronger hooks",
        "Increase audience retention"
    ]

    return {
        "growth_score": 75,
        "opportunity_score": 90,
        "weaknesses": weaknesses,
        "improvements": improvements
    }