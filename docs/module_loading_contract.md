# Module Loading Contract

Purpose  
Defines exactly how modules import each other, what is allowed, and what is forbidden.  
This prevents circular imports and pipeline corruption.

------------------------------------------------------------

## Global Rules

1. Pipelines orchestrate modules.  
2. Modules DO NOT call each other horizontally.  
3. Only pipelines may combine multiple modules at once.  
4. No module may load ONI pipeline logic.  
5. No module may import another module’s internals unless defined below.

------------------------------------------------------------

## Allowed Direction of Imports (Top → Down)

ONI  
    → Baymax  
    → Chrono  
    → VERA  
    → Victor  
    → Utils

Pipelines  
    → ONI  
    → Chrono  
    → VERA  
    → Baymax  
    → Victor  
    → Utils

Routes  
    → Pipelines only  
Routes may NOT import modules directly.

------------------------------------------------------------

## Forbidden

❌ ONI importing pipelines  
❌ VERA importing ONI  
❌ Chrono importing Baymax  
❌ Victor importing pipelines  
❌ Routes calling modules directly  
❌ Pipelines calling routes  
❌ Any circular import across modules

------------------------------------------------------------

## Pipeline Contract

Pipelines MUST:
• Receive input  
• Call modules in sequence  
• Combine outputs  
• Return a complete result  
• Never contain business logic from any module  

------------------------------------------------------------

## Load Order

load order MUST follow:

routes → pipelines → modules → utils

------------------------------------------------------------

END