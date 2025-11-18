from typing import Optional
from anthropic import Anthropic
from .config import get_settings

_claude_client: Optional[Anthropic] = None


def get_claude_client() -> Anthropic:
    global _claude_client
    if _claude_client is not None:
        return _claude_client

    settings = get_settings()
    if not settings.claude_api_key:
        raise RuntimeError("Claude API key is missing")

    _claude_client = Anthropic(api_key=settings.claude_api_key)
    return _claude_client
