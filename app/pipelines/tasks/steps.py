from typing import List, Dict


def break_into_steps(task_text: str) -> List[Dict]:
    """
    Very simple step splitter for the mini project app.
    """
    return [
        {"index": 0, "description": task_text, "status": "todo"},
    ]
