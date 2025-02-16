from typing import Annotated, Literal, TypedDict
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END, START
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
import yaml
from datetime import datetime

from .memory.state import MessagesState
from .tools import get_tools

class AgentGraph:
    def __init__(self, openai_api_key: str, openai_model: str):
        # Load system prompt
        with open('data/prompts/system_prompt.yaml', 'r') as file:
            prompt_config = yaml.safe_load(file)
            self.system_prompt_template = prompt_config['system']

        # Initialize tools
        self.tools = get_tools()
        self.tool_node = ToolNode(tools=self.tools)
        
        self.model = ChatOpenAI(
            api_key=openai_api_key,
            model=openai_model,
            temperature=0.2
        ).bind_tools(self.tools)

        # Initialize graph
        self.workflow = StateGraph(MessagesState)
        
        # Add nodes
        self.workflow.add_node("chatbot", self.chatbot)
        self.workflow.add_node("tools", self.tool_node)
        
        self.workflow.add_edge(START, "chatbot")
        
        self.workflow.add_conditional_edges(
            "chatbot",
            tools_condition,
        )
        
        # Add return edge from tools to chatbot
        self.workflow.add_edge("tools", "chatbot")
        
        # Initialize memory
        self.checkpointer = MemorySaver()
        
        # Compile graph
        self.app = self.workflow.compile(checkpointer=self.checkpointer)

    def get_formatted_system_prompt(self) -> str:
        """Get system prompt with current date inserted"""
        current_date = datetime.now().strftime("%Y-%m-%d")
        return self.system_prompt_template.format(current_date=current_date)

    def chatbot(self, state: MessagesState):
        return {"messages": [self.model.invoke(state["messages"])]}

    def invoke(self, message: str, thread_id: str):
        # Create messages list with system prompt and user message
        messages = [
            {"role": "system", "content": self.get_formatted_system_prompt()},
            {"role": "user", "content": message}
        ]
        
        # Create the initial state dictionary
        state = {"messages": messages}
        
        return self.app.stream(
            state,
            config={"configurable": {"thread_id": thread_id}},
        )