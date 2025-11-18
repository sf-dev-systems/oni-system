"""
Minimal mock parser for the ONI minimal pipeline.
"""

def parse_message(payload: dict) -> dict:
    """
    Minimal mock parser for the ONI minimal pipeline.
    Normalizes input and extracts text + metadata.
    """
    return {
        "raw": payload,
        "text": payload.get("text") or payload.get("content") or "",
        "metadata": payload.get("metadata", {}),
    }
