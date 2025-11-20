from app.chrono.classifier import chrono_classify
from app.pipelines.minimal_models import (
    MinimalIngestRequest,
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
from app.oni.executive import oni_process


def oni_run_minimal_pipeline(text: str) -> dict:
    segment_packet = SegmentPacket(type="single_segment", segments=[text])
    event_packet = chrono_classify(text)
    qa_packet = vera_validate(event_packet)
    storage_record = victor_store(event_packet, qa_packet, qa_packet.corrected_event)
    baymax_packet = baymax_reason(event_packet, qa_packet)
    oni_packet = oni_process(segment_packet, event_packet, qa_packet, baymax_packet)

    return {
        "status": "ok",
        "segment_packet": segment_packet.model_dump(),
        "event_packet": event_packet.model_dump(),
        "qa_packet": qa_packet.model_dump(),
        "storage_record": storage_record.model_dump(),
        "baymax_packet": baymax_packet.model_dump(),
        "oni_packet": oni_packet.model_dump(),
    }
