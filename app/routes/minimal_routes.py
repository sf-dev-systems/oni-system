from fastapi import APIRouter
from pydantic import BaseModel
from app.pipelines.minimal_oni_pipeline import oni_run_minimal_pipeline

minimal_router = APIRouter(prefix="/minimal")

class MinimalIngestRequest(BaseModel):
    text: str
    thread_key: str | None = "default"

@minimal_router.post("/ingest")
async def ingest(req: MinimalIngestRequest):
    return oni_run_minimal_pipeline(req.text, req.thread_key)