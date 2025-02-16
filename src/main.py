import os
from pathlib import Path

# Add the project root to Python path
import sys
project_root = str(Path(__file__).parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)

from fastapi import FastAPI
from src.api.routes import agent
from contextlib import asynccontextmanager
from src.core.settings import settings
from src.agent.graph import AgentGraph

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.agent = AgentGraph(
        openai_api_key=settings.OPENAI_API_KEY,
        openai_model=settings.OPENAI_DEFAULT_MODEL
    )       
    yield

app = FastAPI(title="AI Agent API", lifespan=lifespan)

app.include_router(agent.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 