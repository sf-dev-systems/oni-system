"""
Minimal mock Chrono classifier.
"""

def classify_event(parsed: dict) -> dict:
    """
    Minimal mock Chrono classifier.
    Always returns a basic event_type + confidence.
    """
    return {
        "event_type": "note",
        "confidence": 0.7,
        "parsed": parsed,
    }
