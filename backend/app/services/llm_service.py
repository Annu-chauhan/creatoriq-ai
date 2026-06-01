from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=api_key
)


def analyze_creator(transcript):

    transcript_lower = transcript.lower()

    niche = "General Content"

    if any(word in transcript_lower for word in [
        "python", "coding", "programming",
        "software", "developer", "machine learning",
        "artificial intelligence", "ai"
    ]):
        niche = "Technology"

    elif any(word in transcript_lower for word in [
        "fitness", "workout", "gym",
        "exercise", "weight loss"
    ]):
        niche = "Fitness"

    elif any(word in transcript_lower for word in [
        "business", "startup", "entrepreneur",
        "marketing", "sales"
    ]):
        niche = "Business"

    elif any(word in transcript_lower for word in [
        "study", "education", "student",
        "learning", "course"
    ]):
        niche = "Education"

    elif any(word in transcript_lower for word in [
        "finance", "stock", "investing",
        "money", "crypto"
    ]):
        niche = "Finance"

    audience = "General Audience"

    if niche == "Technology":
        audience = "Developers, Students, Tech Enthusiasts"

    elif niche == "Fitness":
        audience = "Fitness Enthusiasts, Gym Goers"

    elif niche == "Business":
        audience = "Entrepreneurs, Professionals"

    elif niche == "Education":
        audience = "Students and Learners"

    elif niche == "Finance":
        audience = "Investors and Finance Enthusiasts"

    return {
        "source": "fallback",
        "analysis": {
            "content_niche": niche,
            "creator_style": "Informative",
            "target_audience": audience,
            "engagement_hooks": [
                "Direct introduction",
                "Simple language"
            ],
            "strengths": [
                "Easy to understand",
                "Clear communication"
            ],
            "weaknesses": [
                "Limited storytelling",
                "Limited emotional hooks"
            ]
        }
    }