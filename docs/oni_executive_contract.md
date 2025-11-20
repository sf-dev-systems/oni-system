ONI Executive Contract
Purpose

Defines how ONI’s executive module behaves in ONI v2:
thread memory, unresolved tracking, and thread summary.
No additional reasoning, recursion, or directive logic is allowed in this version.

1. File Location

The ONI executive module must live in:

app/oni/executive.py


No other files may define ONI executive behavior.

2. Import Rules

The ONLY permitted imports inside executive.py are:

from typing import Dict, Any
from app.victor.storage import VictorClient


No additional imports may be added unless explicitly allowed by a future contract.

3. Required Functions

The executive MUST define exactly three functions:

3.1 get_or_create_thread(victor, thread_key)

Input

victor: VictorClient

thread_key: str

Output
A dict:

{
    "thread_id": str,
    "state": str
}


Behavior

Call victor.find_thread(thread_key)

If a record exists: return it.

Otherwise call victor.create_thread(thread_key) and return the result.

No caching. No additional logic.

3.2 record_unresolved(victor, thread_id, item)

Input

victor: VictorClient

thread_id: str

item: Dict[str, Any]

Behavior

Call victor.store_unresolved_item(thread_id, item)

Do not mutate anything locally.

Do not return anything.

3.3 summarize_thread(victor, thread_id)

Input

victor: VictorClient

thread_id: str

Output
A dict:

{
    "thread_id": thread_id,
    "unresolved_count": int
}


Behavior

Fetch unresolved items with victor.get_unresolved_items(thread_id)

Count them

Return result

No other fields, no extra computation.

4. Forbidden Behavior

The executive module may NOT:

Create local cache or in-memory thread maps

Manage directives

Detect contradictions

Perform reasoning

Write events directly

Call Chrono, Baymax, VERA, or pipeline functions

Import anything except the approved imports

Create new folders or modules

Define new routes

Modify Victor behavior

Store data outside Victor

Change the shape of returned executive values

5. Required Stability

All functions must:

Keep the exact function names

Keep the exact parameter ordering

Keep the exact return structure

Remain pure wrappers around Victor v2 functionality

Never mutate global state

6. Relationship to Other Modules

Victor v2 handles all persistent storage.

Pipeline is responsible for calling these functions.

Chrono, VERA, Baymax may generate unresolved items but cannot store them.

ONI v2 executive only routes the information to Victor and returns summaries.

7. Compliance

Any code written by Codex, GPT, Claude, Cursor, or other assistants must comply fully with this contract.
If a modification violates any rule above, the change must be rejected.

END OF CONTRACT