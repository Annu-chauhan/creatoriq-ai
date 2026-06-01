from app.services.llm_service import analyze_creator
from app.services.strategy_service import generate_strategy
from app.services.brand_match_service import calculate_brand_match
from app.services.growth_audit_service import generate_growth_audit


def generate_dashboard(transcript):

    creator_analysis = analyze_creator(
        transcript
    )

    content_strategy = generate_strategy(
        transcript,
        creator_analysis
    )

    brand_match = calculate_brand_match(
        transcript,
        creator_analysis,
        "education"
    )

    growth_audit = generate_growth_audit(
        transcript,
        creator_analysis
    )

    creator_health_score = (
        growth_audit["growth_score"]
        +
        brand_match["creator_score"]
    ) // 2

    dashboard_summary = (
        f"{creator_analysis['analysis']['content_niche']} creator "
        f"with {brand_match['brand_fit']} brand fit "
        f"and a health score of {creator_health_score}."
    )

    return {
        "dashboard_summary": dashboard_summary,
        "creator_health_score": creator_health_score,
        "creator_analysis": creator_analysis,
        "content_strategy": content_strategy,
        "brand_match": brand_match,
        "growth_audit": growth_audit
    }