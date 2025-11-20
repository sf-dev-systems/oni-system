from uuid import uuid4
from datetime import datetime, timezone
from typing import Any, Optional

from app.supabase_client import get_supabase_client
from app.pipelines.minimal_models import EventPacket, QAPacket, StorageRecord


def store_event(event_packet: EventPacket):
    client = get_supabase_client()
    payload = {
        "event_id": event_packet.event_id,
        "message_id": event_packet.message_id,
        "session_id": event_packet.session_id,
        "event_type": event_packet.event_type,
        "subtype": event_packet.subtype,
        "intensity": event_packet.intensity,
        "trigger": event_packet.trigger,
        "pattern_shape": event_packet.pattern_shape,
        "context": event_packet.context,
        "content": event_packet.content,
        "module": event_packet.module,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    resp = client.table("events").insert(payload).execute()
    return resp


def store_qa_packet(qa_packet: QAPacket):
    client = get_supabase_client()
    payload = {
        "qa_id": qa_packet.qa_id,
        "event_id": qa_packet.event_id,
        "override": qa_packet.override,
        "reason": qa_packet.reason,
        "corrected_event": qa_packet.corrected_event,
        "request_user_confirmation": qa_packet.request_user_confirmation,
        "timestamp": qa_packet.qa_timestamp or datetime.now(timezone.utc).isoformat(),
    }
    resp = client.table("qa_packets").insert(payload).execute()
    return resp


def store_overrides(event_packet: EventPacket, qa_packet: QAPacket, corrections_list: Optional[list] = None):
    """
    Placeholder for future override logging to qa_overrides table.
    """
    return None


def store_version_entry(event_packet: EventPacket, qa_packet: QAPacket, corrected_event: Optional[dict] = None):
    client = get_supabase_client()
    payload = {
        "version_id": f"ver_{uuid4().hex}",
        "event_id": event_packet.event_id,
        "version_num": 1,
        "qa_packet_snapshot": qa_packet.model_dump(),
        "corrected_event_snapshot": corrected_event,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    resp = client.table("qa_version_history").insert(payload).execute()
    return resp


def victor_store(event_packet: EventPacket, qa_packet: QAPacket, corrected_event: Optional[dict] = None) -> StorageRecord:
    store_event(event_packet)
    store_qa_packet(qa_packet)

    if qa_packet.override:
        store_overrides(event_packet, qa_packet, corrections_list=None)
        store_version_entry(event_packet, qa_packet, corrected_event)

    return StorageRecord(
        storage_id=f"store_{uuid4().hex}",
        event_id=event_packet.event_id,
        qa_id=qa_packet.qa_id,
        stored=True,
        backend="supabase",
    )
