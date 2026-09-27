from langchain_core.messages import SystemMessage

from app.graph.state import ChatState
from app.services.llm import llm


async def chat_node(state: ChatState):
    messages = [
        SystemMessage(
            content="You are a helpful and concise AI assistant."
        ),
        *state["messages"],
    ]

    response = await llm.ainvoke(messages)

    return {
        "messages": [response]
    }