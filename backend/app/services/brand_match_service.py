def calculate_brand_match(
    transcript,
    creator_analysis,
    brand_category
):

    niche = creator_analysis[
        "analysis"
    ]["content_niche"]

    score = 50

    reasons = []

    if niche.lower() in brand_category.lower():

        score += 40

        reasons.append(
            f"Strong alignment with {brand_category}"
        )

    if len(transcript) > 500:

        score += 10

        reasons.append(
            "High content depth"
        )

    recommended_brands = []

    if niche == "Technology":
        recommended_brands = [
            "OpenAI",
            "GitHub",
            "Google Cloud",
            "Microsoft",
            "NVIDIA"
        ]

    elif niche == "Fitness":
        recommended_brands = [
            "Nike",
            "MyProtein",
            "Cult.fit",
            "Adidas",
            "Fitbit"
        ]

    elif niche == "Business":
        recommended_brands = [
            "HubSpot",
            "Notion",
            "Shopify",
            "Zoho",
            "Salesforce"
        ]

    elif niche == "Education":
        recommended_brands = [
            "Coursera",
            "Udemy",
            "Unacademy",
            "Physics Wallah",
            "Scaler"
        ]

    elif niche == "Finance":
        recommended_brands = [
            "Groww",
            "Zerodha",
            "Upstox",
            "Angel One",
            "CoinDCX"
        ]

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
        "sponsorship_potential": "High",
        "recommended_brands": recommended_brands,
        "reasons": reasons
    }