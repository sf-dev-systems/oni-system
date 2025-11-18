from typing import Any, Dict


def dispatch(plan: Dict[str, Any]) -> Dict[str, Any]:
    """
    Stub to represent the dispatcher choosing the next step.
    """
    pipeline = plan.get("suggested_pipeline", "parse")
    return {
        "selected_pipeline": pipeline,
        "reason": "stub_dispatcher",
    }
