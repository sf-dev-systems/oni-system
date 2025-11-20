from datetime import datetime
from typing import Literal
from pydantic import BaseModel


class MinimalIngestRequest(BaseModel):
    text: str


class SegmentPacket(BaseModel):
    type: str
    segments: list[str]


class EventPacket(BaseModel):
    event_id: str
    message_id: str
    session_id: str
    event_type: str
    subtype: str | None = None
    intensity: str | None = None
    trigger: str | None = None
    pattern_shape: str | None = None
    context: dict | None = None
    content: str
    module: str


class QAPacket(BaseModel):
    qa_id: str
    event_id: str
    override: bool
    reason: str | None = None
    corrected_event: dict | None = None
    qa_timestamp: str | None = None
    request_user_confirmation: bool = False
    unresolved: bool = False


class StorageRecord(BaseModel):
    storage_id: str
    event_id: str
    qa_id: str
    stored: bool
    backend: str


class BaymaxPacket(BaseModel):
    baymax_id: str
    event_id: str
    qa_id: str
    reasoning: dict
    timestamp: datetime
    module: Literal["baymax"]


class OniPacket(BaseModel):
    oni_id: str
    event_id: str
    qa_id: str
    baymax_id: str
    directives: dict
    thread_updates: dict
    summary: str
    timestamp: datetime
    module: Literal["oni"] = "oni"
