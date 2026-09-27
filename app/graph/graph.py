from langgraph.graph import START, END, StateGraph

from app.graph.state import ChatState
from app.graph.nodes import chat_node


builder = StateGraph(ChatState)

builder.add_node("chat", chat_node)

builder.add_edge(START, "chat")
builder.add_edge("chat", END)

graph = builder.compile()