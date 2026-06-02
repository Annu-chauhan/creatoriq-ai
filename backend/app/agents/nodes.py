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

    retrieval = retrieve_context(
        state["question"]
    )

    state["context"] = retrieval["context"]

    state["sources"] = retrieval["sources"]

    return state


def answer_node(state):

    prompt = f"""
    You are CreatorIQ AI.

    Previous Conversation:
    {state["chat_history"]}

    Context:
    {state["context"]}

    Question:
    {state["question"]}

    Use the context to answer.

    If relevant, reference information from the retrieved sources.
    Give a detailed answer.
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    answer = response.text

    if state["sources"]:

        answer += "\n\nSources:\n"

        answer += "\n".join(
            state["sources"]
        )

    state["answer"] = answer

    state["chat_history"].append(
        {
            "question": state["question"],
            "answer": response.text
        }
    )

    return state