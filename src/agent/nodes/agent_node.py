from typing import Annotated, Dict, TypedDict
from langchain_core.messages import BaseMessage
from operator import add

def call_model(state: Dict, config: Dict):
    """Agent node that decides whether to use tools or end conversation"""
    messages = state["messages"]
    model = config["model"]
    
    # Get response from the model
    response = model.invoke(messages)
    
    # Check if the model wants to use a tool
    if response.tool_calls:
        # If tool calls present, return tool node
        return {"messages": messages + [response], "next": "tools"}
    
    # If no tool calls, end the conversation
    return {"messages": messages + [response], "next": "__end__"} 