from typing import Any


def to_dict(obj: Any) -> dict:
    """
    Safe dict converter.
    """
    if isinstance(obj, dict):
        return obj
    if hasattr(obj, "model_dump"):
        return obj.model_dump()
    return obj.__dict__ if hasattr(obj, "__dict__") else {"value": obj}
