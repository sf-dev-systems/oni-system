from typing import List, Dict


def segment_text(text: str) -> List[Dict]:
    """
    Very simple segmentation placeholder.
    """
    segments = [s.strip() for s in text.split("\n") if s.strip()]
    return [{"index": i, "content": s} for i, s in enumerate(segments)]
