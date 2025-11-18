from typing import List
from ...openai_client import get_openai_client
from ...config import get_settings


def embed_texts(texts: List[str]) -> List[List[float]]:
    """
    Uses OpenAI embeddings to embed texts.
    """
    client = get_openai_client()
    settings = get_settings()

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts,
    )
    vectors = [item.embedding for item in response.data]
    return vectors
