from uuid import uuid4
from datetime import datetime, timezone
from typing import Any, Optional, Dict, List

from app.supabase_client import get_supabase_client
from app.pipelines.minimal_models import EventPacket, QAPacket, StorageRecord


class VictorClient:
    def __init__(self):
        self.client = get_supabase_client()

    # THREAD LOOKUP
    def find_thread(self, thread_key: str) -> Optional[Dict[str, Any]]:
        resp = (
            self.client.table("threads")
            .select("*")
            .eq("thread_key", thread_key)
            .limit(1)
            .execute()
        )
        if resp.data:
            row = resp.data[0]
            return {"thread_id": row["id"], "state": row["state"]}
        return None

    # THREAD CREATE
    def create_thread(self, thread_key: str) -> Dict[str, Any]:
        payload = {"thread_key": thread_key, "state": "open"}
        resp = self.client.table("threads").insert(payload).execute()
        row = resp.data[0]
        return {"thread_id": row["id"], "state": row["state"]}

    # STORE UNRESOLVED ITEM
    def store_unresolved_item(self, thread_id: str, item: Dict[str, Any]) -> None:
        payload = {
            "thread_id": thread_id,
            "item_type": item.get("type"),
            "content": item.get("payload"),
            "status": item.get("status", "unresolved"),
            "created_at": datetime.utcnow().isoformat(),
        }
        self.client.table("unresolved_items").insert(payload).execute()

    # GET UNRESOLVED ITEMS
    def get_unresolved_items(self, thread_id: str) -> List[Dict[str, Any]]:
        resp = (
            self.client.table("unresolved_items")
            .select("*")
            .eq("thread_id", thread_id)
            .execute()
        )
        return resp.data or []


# STORE EVENT + QA PACKET WITH THREAD_ID
def victor_store_event(event_packet: EventPacket, qa_packet: QAPacket, thread_id: str) -> StorageRecord:
    client = get_supabase_client()

    event_payload = {
        "event_id": event_packet.event_id,
        "message_id": event_packet.message_id,
        "session_id": event_packet.session_id,
        "thread_id": thread_id,
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
    client.table("events").insert(event_payload).execute()

    qa_payload = {
        "qa_id": qa_packet.qa_id,
        "event_id": event_packet.event_id,
        "override": qa_packet.override,
        "reason": qa_packet.reason,
        "corrected_event": qa_packet.corrected_event,
        "request_user_confirmation": qa_packet.request_user_confirmation,
        "timestamp": qa_packet.qa_timestamp or datetime.now(timezone.utc).isoformat(),
    }
    client.table("qa_packets").insert(qa_payload).execute()

    return StorageRecord(
        storage_id=f"store_{uuid4().hex}",
        event_id=event_packet.event_id,
        qa_id=qa_packet.qa_id,
        stored=True,
        backend="supabase",
    )
