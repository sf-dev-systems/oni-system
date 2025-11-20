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
from app.victor.storage import victor_store_event, VictorClient
from app.baymax.reasoner import baymax_reason
from app.oni.executive import (
    get_or_create_thread,
    record_unresolved,
    summarize_thread,
)

victor = VictorClient()

def oni_run_minimal_pipeline(text: str, thread_key: str = "default") -> dict:
    segment_packet = SegmentPacket(type="single_segment", segments=[text])
    event_packet = chrono_classify(text)
    qa_packet = vera_validate(event_packet)

    thread_record = get_or_create_thread(victor, thread_key)
    thread_id = thread_record["thread_id"]

    victor_store_event(event_packet, qa_packet, thread_id)

    baymax_packet = baymax_reason(event_packet, qa_packet)

    if getattr(qa_packet, "unresolved", False):
        record_unresolved(
            victor,
            thread_id,
            {
                "id": event_packet.event_id,
                "type": event_packet.event_type,
                "payload": event_packet.content,
                "status": "unresolved",
            },
        )

    thread_summary = summarize_thread(victor, thread_id)

    return {
        "status": "ok",
        "thread_id": thread_id,
        "unresolved_count": thread_summary["unresolved_count"],
        "segment_packet": segment_packet.model_dump(),
        "event_packet": event_packet.model_dump(),
        "qa_packet": qa_packet.model_dump(),
        "baymax_packet": baymax_packet.model_dump(),
    }
