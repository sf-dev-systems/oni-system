ONI v2 Specification

Purpose
ONI v2 introduces long-term thread memory, directive engines, contradiction clustering, and cross-module executive control.

Core Concepts

thread_id
A stable key assigned to all events in the same conversation or decision process.

thread_state
Possible values:
- open
- blocked
- resolved

unresolved_items
A list of items requiring further action.
Structure:
- id
- type (question | decision)
- payload (json)
- status

directive
Represents ONI instructions that influence pipeline behavior.
Fields:
- directive_id
- source (oni | user | external)
- target_module (chrono | vera | baymax | victor)
- payload (json)
- status

contradiction
Represents a detected inconsistency.
Fields:
- contra_id
- thread_id
- items_in_conflict (json list)
- status (detected | reviewed | resolved)

Interactions
- Chrono may mark unresolved interpretation.
- VERA may mark validation blocks.
- Baymax may request next best question.
- Victor stores all thread activity.
- ONI manages thread lifecycle.

Minimal Requirements for ONI v2
- get_or_create_thread(thread_key)
- record_unresolved(thread_id, item)
- pipeline returns:
    - thread_id
    - unresolved_count

END.
