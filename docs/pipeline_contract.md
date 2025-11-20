Pipeline Contract
Purpose
Defines how all ONI pipelines must be structured, named, imported, and executed.
Covers ONI v2 minimal pipeline requirements only.
Prevents Codex, GPT, Claude, or Cursor from altering or improvising pipeline flow.

1. File Location
All pipeline code must live in:
app/pipelines/

Each pipeline is a Python file ending with:
*_pipeline.py

The minimal pipeline must be:
app/pipelines/minimal_oni_pipeline.py

No additional pipeline folders may be created.

2. Import Rules
A pipeline may import ONLY:
from app.chrono.classifier import chrono_classify
from app.vera.validator import vera_validate
from app.victor.storage import VictorClient, victor_store_event
from app.baymax.reasoner import baymax_reason
from app.oni.executive import get_or_create_thread, record_unresolved, summarize_thread
from app.pipelines.minimal_models import (
    SegmentPacket,
    EventPacket,
    QAPacket,
    StorageRecord,
    BaymaxPacket,
)

No pipeline may import from:
• other pipelines
• ONI directives
• ONI global_state
• utilities outside allowed list
• frontend
• routes
No additional imports permitted without contract updates.

3. Required Function
Each pipeline file MUST expose one public function:
oni_run_minimal_pipeline(text: str, thread_key: str = "default") -> dict

Naming rule:
• Must start with the module name (oni_run_*)
• Must return a dict, not a Pydantic model
No additional entrypoints allowed.

4. Required Execution Flow
All ONI pipelines MUST follow this exact sequence, in this exact order:


Segment Text
Create SegmentPacket with the raw text.


Chrono Classification
Call chrono_classify(text) → returns EventPacket.


VERA Validation
Call vera_validate(event_packet) → returns QAPacket.


Thread Handling (ONI v2)
Call get_or_create_thread(victor, thread_key)
Extract thread_id.


Store Event in Victor
Call:
victor_store_event(event_packet, qa_packet, thread_id)



Baymax Reasoning
Call baymax_reason(event_packet, qa_packet) → returns BaymaxPacket.


Unresolved Tracking
If QAPacket contains unresolved == True:
Call record_unresolved(victor, thread_id, item_dict)
Item dict structure must follow oni_v2_spec.md.


Thread Summary
Call summarize_thread(victor, thread_id).


Return Response
Returned dict MUST include:


{
  "status": "ok",
  "thread_id": thread_id,
  "unresolved_count": int,
  "segment_packet": { ... },
  "event_packet": { ... },
  "qa_packet": { ... },
  "storage_record": { ... },
  "baymax_packet": { ... }
}

No additional keys permitted.

5. Forbidden Behavior
Pipelines MUST NOT:
• perform reasoning
• write data outside Victor
• generate decisions, directives, contradictions
• call ONI executive logic other than the 3 approved functions
• import or modify global state
• call any module other than the allowed sequence
• mutate models directly
• store in-memory threads
• change response field names
No branches, no shortcuts, no reordering.

6. Stability Rules
The pipeline must always:
• Use the same order
• Use the same output structure
• Use Victor for all persistence
• Use ONI executive for all thread interactions
• Avoid caching or global mutable state (except global VictorClient)
• Avoid new optional parameters unless allowed by future contract

7. Contract Priority
If a conflict exists between:


pipeline_contract.md


oni_executive_contract.md


victor_v2_schema.md


oni_v2_spec.md


Then pipeline_contract.md rules override pipeline behavior,
but oni_executive_contract.md governs executive behavior,
and victor_v2_schema.md governs storage behavior.

END OF CONTRACT

When you’re ready:
Say: “Begin Phase 6 – coding.”