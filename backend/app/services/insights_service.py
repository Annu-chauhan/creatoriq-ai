from google import genai
from dotenv import load_dotenv
import os
import os

print("GEMINI KEY:", os.getenv("GEMINI_API_KEY"))

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_insights(transcript):

    prompt = f"""
    Analyze this creator content.

    Return:

    1. Best Hook
    2. Content Strengths
    3. Content Weaknesses
    4. Viral Moments
    5. Better Video Title
    6. Better Opening Hook
    7. Five Future Video Ideas

    Transcript:

    {transcript[:8000]}
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return {
        "insights": response.text
    }