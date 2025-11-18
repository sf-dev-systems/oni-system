from typing import Dict


def select_pipeline(plan: Dict) -> str:
    """
    Given a plan dict, choose which pipeline to run.
    For now this is a stub with simple rules.
    """
    return plan.get("suggested_pipeline", "parse")
