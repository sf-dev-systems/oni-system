"""
Minimal mock Victor storage layer.
"""

def store_event(qa_packet: dict) -> dict:
    """
    Minimal mock Victor storage layer.
    Simulates a DB write and returns an event ID.
    """
    return {
        "stored": True,
        "id": "demo-id-123",
        "qa_packet": qa_packet,
    }
