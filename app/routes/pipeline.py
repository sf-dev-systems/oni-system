from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.chrono import chrono_analyze
from app.agents.vera import vera_review
from app.agents.oni import oni_decide


router = APIRouter(prefix="/pipeline", tags=["pipeline"])


class PipelineRequest(BaseModel):
    text: str


@router.post("/run")
def run_pipeline(payload: PipelineRequest):
    """
    Run the Chrono → VERA → Oni pipeline on the provided text.
    """
    chrono_output = chrono_analyze(payload.text)
    vera_output = vera_review(chrono_output)
    oni_output = oni_decide(chrono_output, vera_output)

    return oni_output
