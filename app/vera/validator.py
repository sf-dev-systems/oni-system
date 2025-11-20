from copy import deepcopy
from datetime import datetime, timezone
from typing import Optional, List, Dict, Any
from uuid import uuid4

from app.pipelines.minimal_models import EventPacket, QAPacket

EVENT_TYPES = {
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

SUBTYPES = {
    "boundary_activation",
    "shutdown",
    "fear",
    "overwhelm",
    "tears",
    "conflict",
}

INTENSITY = {"low", "medium", "high"}

PATTERN_SHAPES = {"approach_avoid", "threshold_fear", "recursion_spiral"}


def _issue(field: str, reason: str, correct_value: Any = None) -> Dict[str, Any]:
    return {"field": field, "reason": reason, "correct_value": correct_value}


def validate_required_fields(event: EventPacket) -> Optional[dict]:
    if not event.event_id or not event.message_id or not event.session_id:
        return _issue("id", "missing_ids", None)
    if not event.content:
        return _issue("content", "missing_content", None)
    if not event.module:
        return _issue("module", "missing_module", "chrono")
    return None


def validate_event_type(event: EventPacket) -> Optional[dict]:
    if event.event_type not in EVENT_TYPES:
        return _issue("event_type", "invalid_event_type", "note")
    return None


def validate_subtype(event: EventPacket) -> Optional[dict]:
    if event.subtype is None:
        return None
    if event.subtype not in SUBTYPES:
        return _issue("subtype", "invalid_subtype", None)
    return None


def validate_intensity(event: EventPacket) -> Optional[dict]:
    if event.intensity is None:
        return None
    if event.intensity not in INTENSITY:
        return _issue("intensity", "invalid_intensity", None)
    return None


def validate_pattern_shape(event: EventPacket) -> Optional[dict]:
    if event.pattern_shape is None:
        return None
    if event.pattern_shape not in PATTERN_SHAPES:
        return _issue("pattern_shape", "invalid_pattern_shape", None)
    return None


def detect_schema_violations(event: EventPacket) -> List[dict]:
    issues = []
    for check in (
        validate_required_fields,
        validate_event_type,
        validate_subtype,
        validate_intensity,
        validate_pattern_shape,
    ):
        result = check(event)
        if result:
            issues.append(result)
    return issues


def detect_hallucinated_fields(event: EventPacket) -> List[dict]:
    issues = []
    if event.module and event.module != "chrono":
        issues.append(_issue("module", "invalid_module", "chrono"))
    return issues


def apply_corrections(event: EventPacket, issues: List[dict]) -> (EventPacket, List[dict]):
    corrected = event.model_copy(deep=True)
    overrides = []
    for issue in issues:
        field = issue["field"]
        reason = issue["reason"]
        correct_value = issue.get("correct_value")

        if field == "id":
            corrected.event_id = f"evt_{uuid4().hex}"
            corrected.message_id = f"msg_{uuid4().hex}"
            corrected.session_id = f"sess_{uuid4().hex}"
            overrides.append({"field": "ids", "new_value": "regenerated", "reason": reason})
            continue

        if field == "module":
            corrected.module = correct_value or "chrono"
        elif field == "event_type":
            corrected.event_type = correct_value or corrected.event_type
        elif field == "subtype":
            corrected.subtype = correct_value
        elif field == "intensity":
            corrected.intensity = correct_value
        elif field == "pattern_shape":
            corrected.pattern_shape = correct_value
        elif field == "content" and correct_value is not None:
            corrected.content = correct_value
        else:
            continue

        overrides.append({"field": field, "new_value": correct_value, "reason": reason})
    return corrected, overrides


def vera_validate(event: EventPacket) -> QAPacket:
    schema_issues = detect_schema_violations(event)
    hallucination_issues = detect_hallucinated_fields(event)
    issues = schema_issues + hallucination_issues

    override = bool(issues)
    corrected_event = None
    override_changes = None
    reason = None
    unresolved = event.event_type == "unresolved question"

    if override:
        reason = issues[0]["reason"] if issues else "schema_violation"
        corrected_event, override_changes = apply_corrections(event, issues)
        corrected_event_dict = corrected_event.model_dump()
    else:
        corrected_event_dict = None

    qa = QAPacket(
        qa_id=str(uuid4()),
        event_id=event.event_id,
        override=override,
        reason=reason,
        corrected_event=corrected_event_dict,
        qa_timestamp=datetime.now(timezone.utc).isoformat(),
        request_user_confirmation=False,
        unresolved=unresolved,
    )
    return qa
