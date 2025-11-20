# Victor v2 Schema Specification

Purpose  
Victor v2 provides durable storage for ONI v2.  
It stores all thread memory, unresolved items, directives, contradictions, events, and QA records.  
This document defines ONLY the database schema, table responsibilities, and required fields.  
No code or behavior is defined here.

------------------------------------------------------------

## Core Tables

Victor v2 MUST contain the following tables:

1. threads  
2. unresolved_items  
3. directives  
3. contradictions  
4. events  
5. qa_packets  
6. qa_version_history

(Events, qa_packets, and qa_version_history already exist in Victor v1. They remain unchanged unless otherwise noted.)

------------------------------------------------------------
## Table: threads

Stores thread lifecycle information for ONI v2.

Columns:
- id (uuid, pk)
- thread_key (text, unique)  
  External identifier used by ONI to find a thread.
- state (text)  
  Values: open | blocked | resolved
- created_at (timestamp)
- updated_at (timestamp)

------------------------------------------------------------
## Table: unresolved_items

Stores unresolved questions or decisions for a given thread.

Columns:
- id (uuid, pk)
- thread_id (uuid, fk → threads.id)
- item_type (text)  
  Values: question | decision
- payload (jsonb)
- status (text)
- created_at (timestamp)

------------------------------------------------------------
## Table: directives

Stores ONI-generated directives that influence downstream modules.

Columns:
- id (uuid, pk)
- thread_id (uuid, fk → threads.id)
- target_module (text)  
  Values: chrono | vera | baymax | victor
- payload (jsonb)
- source (text)  
  Values: oni | user | external
- status (text)
- created_at (timestamp)

------------------------------------------------------------
## Table: contradictions

Stores contradictions detected by ONI or Baymax.

Columns:
- id (uuid, pk)
- thread_id (uuid, fk → threads.id)
- items_in_conflict (jsonb list)
- status (text)  
  Values: detected | reviewed | resolved
- created_at (timestamp)

------------------------------------------------------------
## Existing Tables (unchanged from Victor v1)

### events  
Stores all raw and classified event records.

### qa_packets  
Stores validation output from VERA.

### qa_version_history  
Stores historical versions of QA corrections.

------------------------------------------------------------
## Victor v2 Responsibilities

Victor v2 MUST:
- Store and retrieve threads by thread_key.
- Store unresolved items.
- Store directives.
- Store contradictions.
- Return unresolved items for a given thread_id.
- Return thread records for ONI.
- Maintain referential integrity via foreign keys.
- Provide ordered retrieval (latest first) for thread inspection.

------------------------------------------------------------
## Minimal Required Victor v2 API (used by ONI v2)

Victor MUST provide the following functions:

1. find_thread(thread_key)
2. create_thread(thread_key)
3. store_unresolved_item(thread_id, item)
4. get_unresolved_items(thread_id)

These are required for ONI v2 executive logic.

------------------------------------------------------------

END