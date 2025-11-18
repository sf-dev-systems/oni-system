from typing import Optional
from openai import OpenAI
from .config import get_settings

_openai_client: Optional[OpenAI] = None


def get_openai_client() -> OpenAI:
    global _openai_client
    if _openai_client is not None:
        return _openai_client

    settings = get_settings()
    if not settings.openai_api_key:
        raise RuntimeError("OpenAI API key is missing")

    _openai_client = OpenAI(api_key=settings.openai_api_key)
    return _openai_client
