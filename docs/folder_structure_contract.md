# ONI System Folder Structure Contract

Purpose  
Defines the exact folder layout of the ONI System backend.  
This contract controls WHAT folders exist and WHAT files may live inside them.  
It defines structure only. No behaviors.

------------------------------------------------------------

## Root Layout

ONI_System/
    app/
    docs/
    frontend/
    .well-known/
    run.py
    test_ngrok.ps1

No other folders or files may be added at root without explicit user approval.

------------------------------------------------------------

## app/ Required Subfolders

app/
    main.py
    config.py
    supabase_client.py
    routes/
    pipelines/
    oni/
    chrono/
    baymax/
    vera/
    victor/
    utils/

These subfolders are FIXED.  
Codex and Claude must NOT create new module folders.  
All code must remain inside these defined modules only.

------------------------------------------------------------

## Allowed Contents

### app/routes/
Contains ONLY router files ending in *_routes.py  
No logic. No pipelines. No database calls.

### app/pipelines/
Contains ONLY pipeline orchestration code.  
Pipelines call modules but do not contain module logic.

### app/oni/
ONI executive logic only.  
planning, directive logic, thread reasoning.

### app/chrono/
Chrono classification logic only.

### app/baymax/
Baymax reasoning logic only.

### app/vera/
Validation & QA logic only.

### app/victor/
Persistent storage utilities only.

### app/utils/
Shared helpers such as gpt_bridge.

------------------------------------------------------------

## Forbidden

• No new top-level modules  
• No moving logic between modules  
• No pipelines inside routes  
• No storage code in pipelines  
• No directives inside chrono  
• No expansion outside allowed folders

END