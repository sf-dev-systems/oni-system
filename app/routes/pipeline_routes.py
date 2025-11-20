from fastapi import APIRouter
from pydantic import BaseModel

from app.utils.gpt_bridge import call_model


router = APIRouter(prefix="/pipeline", tags=["pipeline"])


class PipelineRequest(BaseModel):
    text: str


@router.post("/run")
def run_pipeline(payload: PipelineRequest):
    """
    Run the placeholder pipeline and bridge to the GPT stub.
    Later this can orchestrate Chrono/VERA/Oni again.
    """
    model_output = call_model(payload.text)
    return {"processed": True, "input": payload.text, "model_output": model_output}
