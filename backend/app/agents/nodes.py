from google import genai
from dotenv import load_dotenv
import os

from app.services.retriever_service import (
    retrieve_context
)

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def retrieve_node(state):

    context = retrieve_context(
        state["question"]
    )

    state["context"] = context

    return state


def answer_node(state):

    prompt = f"""
    You are CreatorIQ AI.

    Use the retrieved context to answer the question.

    Context:
    {state["context"]}

    Question:
    {state["question"]}

    Give a detailed answer.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    state["answer"] = response.text

    return state