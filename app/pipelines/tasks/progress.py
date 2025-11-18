from typing import List, Dict


def mark_step_done(steps: List[Dict], index: int) -> List[Dict]:
    updated = []
    for step in steps:
        if step["index"] == index:
            step = {**step, "status": "done"}
        updated.append(step)
    return updated
