from typing import Any, Dict, List


def plan_goal(user_input: str) -> Dict[str, Any]:
    """
    High level planning for ONI.
    Returns a simple dict with:
    - goals: list of goals
    - suggested_pipeline: name of pipeline to run
    """
    return {
        "input": user_input,
        "goals": ["understand_intent", "select_pipeline"],
        "suggested_pipeline": "parse",
    }
