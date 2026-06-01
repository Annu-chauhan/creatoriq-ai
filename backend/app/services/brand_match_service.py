def calculate_brand_match(transcript, brand_category):

    brand_category = brand_category.lower()

    score = 50
    reasons = []

    if brand_category == "education":
        score += 30
        reasons.append(
            "Educational and informative content"
        )

    if len(transcript) > 500:
        score += 10
        reasons.append(
            "Sufficient content depth"
        )

    score = min(score, 100)

    if score >= 80:
        brand_fit = "High"
    elif score >= 60:
        brand_fit = "Medium"
    else:
        brand_fit = "Low"

    return {
        "creator_score": score,
        "brand_fit": brand_fit,
        "audience_match": "Good",
        "sponsorship_potential": "Medium",
        "reasons": reasons
    }