from app.chrono.classifier import chrono_classify
from app.pipelines.minimal_models import (
    SegmentPacket,
    EventPacket,
    QAPacket,
    StorageRecord,
    BaymaxPacket,
    OniPacket,
)
from app.vera.validator import vera_validate
from app.victor.storage import victor_store
from app.baymax.reasoner import baymax_reason
from app.oni.executive import (
    get_or_create_thread,
    record_unresolved,
    summarize_thread,
)

def oni_run_minimal_pipeline(text: str, thread_key: str = "default") -> dict:
    """
    Option A pipeline.
    Uses existing Victor v1 storage and ONI v2 executive logic.
    Adds:
        - thread_id
        - unresolved tracking
        - unresolved_count summary
    """

    # 1. Chrono segmentation
    segment_packet = SegmentPacket(type="single_segment", segments=[text])

    # 2. Chrono classification
    event_packet = chrono_classify(text)

    # 3. VERA validation
    qa_packet = vera_validate(event_packet)

    # 4. Get thread record (ONI v2)
    thread_record = get_or_create_thread(thread_key)
    thread_id = thread_record["thread_id"]

    # 5. Victor store event + QA (same as v1)
    storage_record = victor_store(
        event_packet=event_packet,
        qa_packet=qa_packet,
        corrected_event=qa_packet.corrected_event
    )

    # 6. Baymax reasoning
    baymax_packet = baymax_reason(event_packet, qa_packet)

    # 7. Minimal unresolved tracking (only if VERA indicates unresolved)
    if getattr(qa_packet, "unresolved", False):
        record_unresolved(
            thread_id,
            {
                "id": event_packet.event_id,
                "type": event_packet.event_type,
                "payload": event_packet.content,
                "status": "unresolved",
            }
        )

    # 8. Thread summary
    thread_summary = summarize_thread(thread_id)

    # 9. Return full output
    return {
        "status": "ok",
        "thread_id": thread_id,
        "unresolved_count": thread_summary["unresolved_count"],
        "segment_packet": segment_packet.model_dump(),
        "event_packet": event_packet.model_dump(),
        "qa_packet": qa_packet.model_dump(),
        "storage_record": storage_record.model_dump(),
        "baymax_packet": baymax_packet.model_dump(),
    }