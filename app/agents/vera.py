from typing import Dict, List


def vera_review(chrono_output: Dict) -> Dict:
    """
    VERA: lightweight review and basic checks.
    This is placeholder logic that can later be swapped for GPT/Claude.
    """
    segments: List[Dict] = chrono_output.get("segments", [])

    flags = []
    for seg in segments:
        text = seg["raw"]
        if len(text) > 200:
            flags.append(
                {
                    "segment_id": seg["id"],
                    "type": "length_warning",
                    "message": "Segment is quite long, consider splitting it.",
                }
            )

    return {
        "summary": "VERA completed review",
        "flag_count": len(flags),
        "flags": flags,
    }
