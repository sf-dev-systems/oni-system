# Simple in-memory global state for ONI v2

global_threads = {}
unresolved = {}
contradictions = {}


def record_decision(event_id: str, text: str):
    global_threads[event_id] = {"type": "decision", "text": text}


def record_unresolved(event_id: str, text: str):
    unresolved[event_id] = {"type": "unresolved", "text": text}


def record_contradiction(event_id: str, reason: str):
    contradictions[event_id] = {"type": "contradiction", "reason": reason}


def get_state():
    return {
        "threads": global_threads,
        "unresolved": unresolved,
        "contradictions": contradictions,
    }
