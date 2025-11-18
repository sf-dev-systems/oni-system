from fastapi import APIRouter
from app.minimal_understanding_block import parse_message
from app.minimal_chrono import classify_event
from app.minimal_vera import qa_check
from app.minimal_victor import store_event

router = APIRouter(prefix="/minimal")

@router.post("/ingest")
async def ingest(payload: dict):
    parsed = parse_message(payload)
    classified = classify_event(parsed)
    qa = qa_check(classified)
    stored = store_event(qa)
    return {
        "parsed": parsed,
        "classified": classified,
        "qa": qa,
        "stored": stored
    }

