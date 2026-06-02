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
            model="gemini-3.5-flash",
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
            "python",
            "coding",
            "programming",
            "software",
            "developer",
            "machine learning",
            "ai"
        ]):
            niche = "Technology"

        elif any(word in transcript_lower for word in [
            "fitness",
            "gym",
            "workout"
        ]):
            niche = "Fitness"

        elif any(word in transcript_lower for word in [
            "business",
            "startup",
            "marketing"
        ]):
            niche = "Business"

        elif any(word in transcript_lower for word in [
            "education",
            "study",
            "student"
        ]):
            niche = "Education"

        elif any(word in transcript_lower for word in [
            "finance",
            "stocks",
            "crypto"
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

def compare_creators(
    transcript_a,
    transcript_b
):

    try:

        prompt = f"""
        Compare these two creator videos.

        VIDEO A:
        {transcript_a[:6000]}

        VIDEO B:
        {transcript_b[:6000]}

        Analyze:

        1. Hook Comparison
        2. Audience Comparison
        3. Content Style Comparison
        4. Which video is likely to get better engagement and why
        5. What Video B can learn from Video A
        6. Growth Recommendations

        Return clean readable text.
        """

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return {
            "comparison": response.text
        }

    except Exception as e:

        print("COMPARE ERROR:", e)

        return {
            "comparison":
            "Comparison could not be generated."
        }