from typing import Any, Dict, List


def verify_payload(payload: Dict[str, Any]) -> List[str]:
    """
    Basic QA stub.
    Returns list of warnings.
    """
    warnings: List[str] = []
    if "original_text" not in payload:
        warnings.append("missing_original_text")
    return warnings
