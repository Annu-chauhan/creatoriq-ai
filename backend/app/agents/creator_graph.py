from langgraph.graph import (
    StateGraph,
    START,
    END
)

from langgraph.checkpoint.memory import MemorySaver

from app.agents.state import CreatorState
from app.agents.nodes import (
    retrieve_node,
    answer_node
)

builder = StateGraph(CreatorState)

builder.add_node("retrieve", retrieve_node)
builder.add_node("answer", answer_node)

builder.add_edge(START, "retrieve")
builder.add_edge("retrieve", "answer")
builder.add_edge("answer", END)

memory = MemorySaver()

graph = builder.compile(
    checkpointer=memory
)