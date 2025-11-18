from typing import Dict


def oni_decide(chrono_output: Dict, vera_output: Dict) -> Dict:
    """
    Oni: integrates Chrono + VERA into a single response.
    Later this can call LLMs; for now it runs locally.
    """
    segment_count = chrono_output.get("segment_count", 0)
    flag_count = vera_output.get("flag_count", 0)

    high_level = []

    if segment_count == 0:
        high_level.append("No actionable text detected.")
    elif segment_count == 1:
        high_level.append("Single item detected. Treat it as one mini project or note.")
    else:
        high_level.append(
            f"{segment_count} items detected. Consider turning them into a mini project checklist."
        )

    if flag_count > 0:
        high_level.append(
            f"VERA raised {flag_count} warning(s). Review those before execution."
        )

    if not high_level:
        high_level.append("Input looks manageable. You can proceed to next steps.")

    return {
        "summary": "Oni integrated Chrono + VERA outputs.",
        "high_level": high_level,
        "chrono": chrono_output,
        "vera": vera_output,
    }
