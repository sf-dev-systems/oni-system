def build_directives(event_packet, qa_packet, baymax_packet):
    directives = {}

    if baymax_packet.reasoning.get("contradiction_detected"):
        directives["contradiction"] = True

    if qa_packet.override:
        directives["recheck"] = True

    return directives
