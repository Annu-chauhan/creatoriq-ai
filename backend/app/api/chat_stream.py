from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.models.chat import ChatRequest
from app.agents.creator_graph import graph

router = APIRouter()


@router.post("/chat")
async def chat(request: ChatRequest):

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


@router.post("/chat-stream")
async def chat_stream(
    request: ChatRequest
):

    def generate():

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

        answer = result["answer"]

        for word in answer.split():

            yield word + " "

    return StreamingResponse(
        generate(),
        media_type="text/plain"
    )