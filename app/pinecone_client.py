from typing import Optional
from pinecone import Pinecone
from .config import get_settings

_pinecone: Optional[Pinecone] = None


def get_pinecone() -> Pinecone:
    global _pinecone
    if _pinecone is not None:
        return _pinecone

    settings = get_settings()
    if not settings.pinecone_api_key:
        raise RuntimeError("Pinecone API key is missing")

    _pinecone = Pinecone(api_key=settings.pinecone_api_key)
    return _pinecone
