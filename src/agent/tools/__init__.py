from langchain_core.tools import Tool
from typing import List
import datetime
import aiohttp
import asyncio
from src.core.settings import settings

async def perplexity_research(query: str) -> str:
    """
    Perform financial research using Perplexity AI API
    Args:
        query: Research query about financial sector/companies
    Returns:
        Research results as a string
    """
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {settings.PERPLEXITY_API_KEY}'
    }
    
    payload = {
        'model': 'llama-3.1-sonar-small-128k-online',
        'messages': [
            {
                'role': 'system',
                'content': 'You are a Financial expert searching for information about a given sector and/or list of companies for Report analysis'
            },
            {
                'role': 'user',
                'content': query
            }
        ]
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                'https://api.perplexity.ai/chat/completions',
                headers=headers,
                json=payload
            ) as response:
                if response.status != 200:
                    return f"Error: API request failed with status {response.status}"
                data = await response.json()
                return data.get('choices', [{}])[0].get('message', {}).get('content', 'No results found')
    except Exception as e:
        return f"Error performing research: {str(e)}"


def get_tools() -> List[Tool]:
    """Return list of available tools for financial analysis"""
    return [
        Tool(
            name="perplexity_research",
            description="Search for financial information about sectors and companies",
            func=lambda x: asyncio.run(perplexity_research(x))
        )
    ]   
