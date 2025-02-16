# AI Agent Project

This project implements an AI agent system with a REST API interface.

## Project Structure

```
.
├── src/
│   ├── agent/
│   │   ├── graph.py         # Agent's knowledge graph implementation
│   │   └── tools/           # Agent tools and utilities
│   ├── api/
│   │   ├── routes/
│   │   │   └── agent.py     # API route handlers for agent endpoints
│   │   └── __init__.py      # API initialization
│   ├── schemas/
│   │   └── chat.py          # Data models and schemas
│   └── main.py              # Application entry point
├── data/
│   └── prompts/
│       └── system_prompt.yaml # System prompts configuration
```

## Installation

1. Create and activate a virtual environment (recommended):
```bash
conda create -n ai-agent python=3.12
conda activate ai-agent
```

2. Install dependencies:
```bash
pip install poetry
poetry install --no-root
```
3. Fill in the environment variables in the `.env` file

## Running the AI Agent

1. Start the server:
```bash
export PYTHONPATH=./
poetry run python src/main.py
```

2. The API will be available at `http://localhost:8000` by default

3. Use the following endpoints:
- POST `/api/v1/chat` - Interact with the AI agent

## Development

To contribute to this project:

1. Clone the repository
2. Create a new branch for your feature
3. Install development dependencies:
```bash
pip install poetry
poetry install --no-root
```