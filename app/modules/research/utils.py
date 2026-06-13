from openai import OpenAI
from tavily import TavilyClient
from app.core.settings import settings

oai_client = OpenAI(base_url=settings.openrouter_base_url, api_key=settings.openrouter_api_key)
tavily_client = TavilyClient(api_key=settings.tavily_api_key)