from fastapi import APIRouter
from app.pipelines.minimal_oni_pipeline import (
    MinimalIngestRequest,
    oni_run_minimal_pipeline,
)

router = APIRouter(prefix="/minimal", tags=["Minimal ONI"])


@router.post("/ingest")
async def ingest_minimal(request: MinimalIngestRequest):
    result = oni_run_minimal_pipeline(request.text)
    return result
