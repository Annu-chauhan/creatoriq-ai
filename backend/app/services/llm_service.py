from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_creator(transcript):

    try:

        prompt = f"""
        Analyze this YouTube creator transcript.

        Return JSON only.

        {{
            "content_niche": "",
            "creator_style": "",
            "target_audience": "",
            "engagement_hooks": [],
            "strengths": [],
            "weaknesses": []
        }}

        Transcript:
        {transcript[:8000]}
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text = response.text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()

        analysis = json.loads(text)

        return {
            "source": "gemini",
            "analysis": analysis
        }

    except Exception as e:

        print("Gemini failed:", e)

        transcript_lower = transcript.lower()

        niche = "General Content"

        if any(word in transcript_lower for word in [
            "python", "coding", "programming",
            "software", "developer",
            "machine learning", "ai"
        ]):
            niche = "Technology"

        elif any(word in transcript_lower for word in [
            "fitness", "gym", "workout"
        ]):
            niche = "Fitness"

        elif any(word in transcript_lower for word in [
            "business", "startup", "marketing"
        ]):
            niche = "Business"

        elif any(word in transcript_lower for word in [
            "education", "study", "student"
        ]):
            niche = "Education"

        elif any(word in transcript_lower for word in [
            "finance", "stocks", "crypto"
        ]):
            niche = "Finance"

        return {
            "source": "fallback",
            "analysis": {
                "content_niche": niche,
                "creator_style": "Informative",
                "target_audience": "General Audience",
                "engagement_hooks": [
                    "Direct introduction"
                ],
                "strengths": [
                    "Clear communication"
                ],
                "weaknesses": [
                    "Limited storytelling"
                ]
            }
        }