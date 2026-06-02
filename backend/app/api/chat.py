from fastapi import APIRouter

from app.models.chat import (
    ChatRequest
)

from app.agents.creator_graph import (
    graph
)

router = APIRouter()


@router.post("/chat")
async def chat(
    request: ChatRequest
):

    result = graph.invoke(
        {
            "question": request.question,
            "context": "",
            "answer": "",
            "sources": [],
            "chat_history": []
        },
        config={
            "configurable": {
                "thread_id": "creatoriq"
            }
        }
    )

    return {
        "answer": result["answer"],
        "sources": result["sources"]
    }