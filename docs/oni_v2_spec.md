# ONI v2 Specification

Purpose  
ONI v2 introduces persistent thread memory, unresolved-item tracking, contradiction clustering, directive handling, and cross-module executive logic.  
This document defines ONLY the data model and responsibilities of ONI v2.  
It does NOT define pipelines or code.

------------------------------------------------------------

## Core Concepts

### thread_id
A persistent identifier that binds all related events, decisions, and validations into a single thread.  
All ONI v2 operations revolve around the thread_id.

### thread_state
Represents the lifecycle stage of a thread.

Values:
- open
- blocked
- resolved

### unresolved_items
A list of questions or decisions that require further action.

Each item has:
- id
- type (question | decision)
- payload (json)
- status

### directive
A structured instruction created by ONI that alters the behavior of downstream modules.

Fields:
- directive_id
- source (oni | user | external)
- target_module (chrono | vera | baymax | victor)
- payload (json)
- status

### contradiction
Represents inconsistencies detected across events, decisions, or reasoning outputs.

Fields:
- contra_id
- thread_id
- items_in_conflict (json list)
- status (detected | reviewed | resolved)

------------------------------------------------------------

## Interactions with Modules

### Chrono
May produce events that contain ambiguity → unresolved_items.

### VERA
May mark validation failures or unclear classifications → unresolved_items.

### Baymax
May identify:
- contradiction patterns
- “next best question”
- missing context

### Victor
Stores ALL thread-level records:
- threads
- unresolved_items
- directives
- contradictions
- events
- qa_packets
- version history

### ONI
Manages thread lifecycle:
- creates or loads thread_id
- appends unresolved_items
- assigns directives
- registers contradictions
- provides thread summary to pipeline

------------------------------------------------------------

## Minimal Requirements for ONI v2

ONI v2 MUST provide three core executive functions:

### 1. get_or_create_thread(thread_key)
Returns existing thread or creates a new one.

### 2. record_unresolved(thread_id, item)
Stores unresolved questions/decisions for a thread.

### 3. summarize_thread(thread_id)
Returns:
- thread_id
- unresolved_count

------------------------------------------------------------

## Pipeline Requirements

Every pipeline using ONI v2 MUST return:
- thread_id
- unresolved_count

ONI v2 logic MUST NOT modify pipelines other than:
- generating thread_id
- tracking unresolved items
- returning thread summary

------------------------------------------------------------

END