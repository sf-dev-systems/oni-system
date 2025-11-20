from fastapi import APIRouter

minimal_router = APIRouter(prefix="/minimal")


@minimal_router.post("/ingest")
async def ingest(payload: dict):
    text = payload.get("text", "")
    return {"received_text": text}
