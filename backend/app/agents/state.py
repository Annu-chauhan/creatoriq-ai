from typing import TypedDict


class CreatorState(
    TypedDict
):

    question: str

    context: str

    answer: str

    sources: list

    chat_history: list