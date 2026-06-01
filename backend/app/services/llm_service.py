from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=api_key
)


def analyze_creator(transcript):

    prompt = f"""
You are a Creator Intelligence Analyst.

Analyze the following transcript and provide:

1. Content Niche
2. Creator Style
3. Target Audience
4. Engagement Hooks
5. Creator Strengths
6. Creator Weaknesses

Transcript:
{transcript}
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return {
            "source": "gemini",
            "analysis": response.text
        }

    except Exception:

        return {
            "source": "fallback",
            "analysis": {
                "content_niche": "General Content",
                "creator_style": "Informative",
                "target_audience": "General Audience",
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