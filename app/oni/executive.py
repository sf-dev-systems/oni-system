from uuid import uuid4
from datetime import datetime, timezone

from app.pipelines.minimal_models import (
    SegmentPacket,
    EventPacket,
    QAPacket,
    BaymaxPacket,
    OniPacket,
)
from app.oni.global_state import (
    record_decision,
    record_unresolved,
    record_contradiction,
)
from app.oni.directives import build_directives


def oni_process(
    segment_packet: SegmentPacket,
    event_packet: EventPacket,
    qa_packet: QAPacket,
    baymax_packet: BaymaxPacket,
) -> OniPacket:
    directives = build_directives(event_packet, qa_packet, baymax_packet)

    text_lower = event_packet.content.lower()
    thread_updates = {
        "decision": False,
        "unresolved": False,
        "contradiction": False,
    }

    if event_packet.event_type == "decision":
        record_decision(event_packet.event_id, event_packet.content)
        thread_updates["decision"] = True

    if directives.get("contradiction"):
        record_contradiction(event_packet.event_id, "contradiction_detected")
        thread_updates["contradiction"] = True

    if "not sure" in text_lower or "maybe" in text_lower:
        record_unresolved(event_packet.event_id, event_packet.content)
        thread_updates["unresolved"] = True

    summary = (
        f"Event {event_packet.event_type}, subtype={event_packet.subtype}, "
        f"intensity={event_packet.intensity}, qa_override={qa_packet.override}, "
        f"tension={baymax_packet.reasoning.get('tension_score')}, "
        f"contradiction={baymax_packet.reasoning.get('contradiction_detected')}"
    )

    return OniPacket(
        oni_id=f"oni_{uuid4().hex}",
        event_id=event_packet.event_id,
        qa_id=qa_packet.qa_id,
        baymax_id=baymax_packet.baymax_id,
        directives=directives,
        thread_updates=thread_updates,
        summary=summary,
        timestamp=datetime.now(timezone.utc),
        module="oni",
    )
