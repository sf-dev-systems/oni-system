from typing import Dict, Any
from app.victor.storage import VictorClient

"""
ONI v2 Executive Logic

Responsibilities:
- Manage thread memory using Victor v2 tables
- Assign or retrieve thread_id for each pipeline request
- Record unresolved items detected by Chrono or VERA
- Provide minimal thread state summary
"""

def get_or_create_thread(victor: VictorClient, thread_key: str) -> Dict[str, Any]:
    """
    Finds an existing thread in Victor or creates a new one.

    Returns:
        {
            "thread_id": str,
            "state": str
        }
    """
    existing = victor.find_thread(thread_key)
    if existing:
        return existing

    return victor.create_thread(thread_key)

def record_unresolved(victor: VictorClient, thread_id: str, item: Dict[str, Any]) -> None:
    """
    Stores an unresolved item (question or decision) associated with a thread.
    """
    victor.store_unresolved_item(thread_id, item)

def summarize_thread(victor: VictorClient, thread_id: str) -> Dict[str, Any]:
    """
    Provides a minimal summary of the thread for ONI v2 output.

    Returns:
        {
            "thread_id": ...,
            "unresolved_count": int
        }
    """
    unresolved = victor.get_unresolved_items(thread_id)
    return {
        "thread_id": thread_id,
        "unresolved_count": len(unresolved)
    }