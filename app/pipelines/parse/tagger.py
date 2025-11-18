from typing import List


def basic_tagger(text: str) -> List[str]:
    """
    Very simple tagger stub.
    """
    tags: List[str] = []
    if "task" in text.lower():
        tags.append("task")
    if "note" in text.lower():
        tags.append("note")
    return tags
