from uuid import uuid4
from datetime import datetime, timezone
from typing import Optional

from app.pipelines.minimal_models import EventPacket, QAPacket, BaymaxPacket


def baymax_reason(event_packet: EventPacket, qa_packet: QAPacket) -> BaymaxPacket:
    reasoning = {}

    # Emotional analysis
    reasoning["emotional_signal"] = event_packet.subtype
    reasoning["intensity"] = event_packet.intensity

    # Tension score heuristic
    if event_packet.intensity == "high":
        reasoning["tension_score"] = 3
    elif event_packet.intensity == "medium":
        reasoning["tension_score"] = 2
    else:
        reasoning["tension_score"] = 1

    # Pattern cues
    reasoning["pattern_shape"] = event_packet.pattern_shape

    # Contradiction rules
    contradiction = False
    text = event_packet.content.lower()
    if event_packet.event_type == "decision" and (
        "not sure" in text or "maybe" in text or "i don't know" in text
    ):
        contradiction = True
    if event_packet.subtype == "shutdown" and event_packet.intensity == "high":
        contradiction = True
    reasoning["contradiction_detected"] = contradiction

    # Context summary
    reasoning["context_summary"] = {
        "length": len(event_packet.content),
        "has_exclamation": "!" in event_packet.content,
        "has_question": "?" in event_packet.content,
        "subtype": event_packet.subtype,
        "pattern_shape": event_packet.pattern_shape,
    }

    return BaymaxPacket(
        baymax_id=f"baymax_{uuid4().hex}",
        event_id=event_packet.event_id,
        qa_id=qa_packet.qa_id,
        reasoning=reasoning,
        timestamp=datetime.now(timezone.utc),
        module="baymax",
    )
