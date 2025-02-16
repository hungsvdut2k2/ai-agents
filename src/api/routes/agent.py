from fastapi import APIRouter, Request
from src.schemas.chat import ChatRequest, ChatResponse

router = APIRouter()

@router.post("/chat")
async def chat(
    body: ChatRequest,
    request: Request
):
    agent = request.app.state.agent
    response = agent.invoke(
        message=body.message,
        thread_id=body.thread_id
    )
    final_response = []
    for event in response:
        final_response.append(event)
    return ChatResponse(
        message=final_response[-1]["chatbot"]["messages"][-1].content,
        thread_id=body.thread_id
    )