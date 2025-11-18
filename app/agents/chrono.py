from typing import List, Dict


def chrono_analyze(text: str) -> Dict:
    """
    Chrono: take raw text and break it into structured units.
    For now this is a simple, local heuristic so it works without external APIs.
    """
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    segments: List[Dict] = []
    for idx, line in enumerate(lines, start=1):
        segments.append(
            {
                "id": idx,
                "raw": line,
                "length": len(line),
            }
        )

    return {
        "summary": f"{len(segments)} segment(s) detected",
        "segment_count": len(segments),
        "segments": segments,
    }
