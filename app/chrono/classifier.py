from uuid import uuid4
from typing import Optional
from app.pipelines.minimal_models import EventPacket

ALLOWED_EVENT_TYPES = {
    "idea",
    "note",
    "decision",
    "update",
    "ontology change",
    "module change",
    "dependency shift",
    "conflict",
    "contradiction",
    "drift alert",
    "unresolved question",
    "version bump",
    "emotional_pattern_event",
}

ALLOWED_SUBTYPES = {
    "boundary_activation",
    "shutdown",
    "fear",
    "overwhelm",
    "tears",
    "conflict",
}

ALLOWED_INTENSITIES = {"low", "medium", "high"}
ALLOWED_PATTERN_SHAPES = {"approach_avoid", "threshold_fear", "recursion_spiral"}


def classify_event_type(text: str) -> str:
    lower = text.lower()
    if "lock this in" in lower or "decide" in lower:
        return "decision"
    if "update:" in lower or "status:" in lower or "update " in lower:
        return "update"
    if "ontology" in lower:
        return "ontology change"
    if "module" in lower:
        return "module change"
    if "drift" in lower:
        return "drift alert"
    if "version" in lower:
        return "version bump"
    if "unresolved" in lower or "i don't know" in lower:
        return "unresolved question"
    return "note"


def classify_subtype(text: str) -> Optional[str]:
    lower = text.lower()
    if "boundary" in lower or "respect my boundary" in lower:
        return "boundary_activation"
    if "shut down" in lower or "shutdown" in lower or "checking out" in lower:
        return "shutdown"
    if "scared" in lower or "afraid" in lower or "fear" in lower:
        return "fear"
    if "overwhelmed" in lower or "too much" in lower:
        return "overwhelm"
    if "crying" in lower or "tears" in lower:
        return "tears"
    if "fight" in lower or "argue" in lower or "conflict" in lower:
        return "conflict"
    return None


def classify_intensity(text: str) -> Optional[str]:
    all_caps_words = [
        w for w in text.split() if any(c.isalpha() for c in w) and w.isupper() and len(w) > 1
    ]
    lower = text.lower()
    if "!!!" in text or len(all_caps_words) > 1:
        return "high"
    strong_words = {"furious", "devastated", "rage", "panic"}
    if "!" in text or any(word in lower for word in strong_words):
        return "medium"
    return "low"


def classify_pattern_shape(text: str) -> Optional[str]:
    lower = text.lower()
    if "back and forth" in lower or "i go in circles" in lower:
        return "recursion_spiral"
    if "starting then stopping" in lower or "approach then avoid" in lower:
        return "approach_avoid"
    if "threshold" in lower or "right before i start" in lower or "freeze at the start" in lower:
        return "threshold_fear"
    return None


def detect_trigger(text: str) -> Optional[str]:
    lower = text.lower()
    if "email" in lower:
        return "email"
    if "phone" in lower:
        return "phone"
    if "family" in lower:
        return "family"
    return None


def build_context(text: str) -> dict:
    return {
        "raw_length": len(text),
        "has_exclamation": "!" in text,
        "has_question": "?" in text,
    }


def chrono_classify(text: str) -> EventPacket:
    """
    Chrono v1: rule-based classifier to produce an EventPacket.
    """
    event_type = classify_event_type(text)
    subtype = classify_subtype(text)
    intensity = classify_intensity(text)
    trigger = detect_trigger(text)
    pattern_shape = classify_pattern_shape(text)
    context = build_context(text)

    event_id = f"evt_{uuid4().hex}"
    message_id = f"msg_{uuid4().hex}"
    session_id = f"sess_{uuid4().hex}"

    return EventPacket(
        event_id=event_id,
        message_id=message_id,
        session_id=session_id,
        event_type=event_type,
        subtype=subtype,
        intensity=intensity,
        trigger=trigger,
        pattern_shape=pattern_shape,
        context=context,
        content=text,
        module="chrono",
    )
