from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage
from operator import add

class MessagesState(TypedDict):
    messages: Annotated[list[BaseMessage], add] 