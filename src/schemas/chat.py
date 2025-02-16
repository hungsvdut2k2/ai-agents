from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    thread_id: str

class ChatResponse(BaseModel):
    message: str 
    thread_id: str 