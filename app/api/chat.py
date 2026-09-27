from fastapi import APIRouter

from langchain_core.messages import HumanMessage

from app.models.chat import ChatRequest
from app.graph.graph import graph


router = APIRouter(prefix="/api/chat", tags=["chat"])


@router.post("")
async def chat(request: ChatRequest):
    result = await graph.ainvoke(
        {
            "messages": [
                HumanMessage(content=request.message)
            ]
        }
    )

    response = result["messages"][-1]

    return {
        "message": response.content
    }