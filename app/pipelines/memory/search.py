from typing import List, Dict, Any
from ...pinecone_client import get_pinecone
from ...config import get_settings


def search_memory(query_vector: List[float], top_k: int = 5) -> List[Dict[str, Any]]:
    """
    Pinecone vector search stub.
    """
    settings = get_settings()
    pc = get_pinecone()

    if not settings.pinecone_index:
        raise RuntimeError("Pinecone index name missing")

    index = pc.Index(settings.pinecone_index)
    res = index.query(vector=query_vector, top_k=top_k, include_metadata=True)

    return [
        {
            "id": match.id,
            "score": match.score,
            "metadata": match.metadata,
        }
        for match in res.matches
    ]
