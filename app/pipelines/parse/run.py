from typing import Dict, Any
from ...agents.chrono_agent.structure import segment_text
from ...agents.baymax.meaning import analyze_meaning
from ...agents.vera_agent.qa import verify_payload
from .clean_text import basic_clean
from .tagger import basic_tagger


def run_parse_pipeline(raw_text: str) -> Dict[str, Any]:
    cleaned = basic_clean(raw_text)
    segments = segment_text(cleaned)
    meaning = analyze_meaning(cleaned)
    tags = basic_tagger(cleaned)

    payload: Dict[str, Any] = {
        "original_text": raw_text,
        "clean_text": cleaned,
        "segments": segments,
        "meaning": meaning,
        "tags": tags,
    }

    warnings = verify_payload(payload)
    payload["warnings"] = warnings

    return payload
