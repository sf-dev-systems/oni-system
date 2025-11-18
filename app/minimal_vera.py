"""
Minimal mock VERA QA check.
"""

def qa_check(classified: dict) -> dict:
    """
    Minimal mock VERA QA check.
    Always passes validation with no override.
    """
    return {
        "qa_passed": True,
        "override": False,
        "reason": None,
        "classified": classified,
    }
