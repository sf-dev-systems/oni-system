TITLE: ONI System Folder Structure Contract
INDEX

Root layout

Required subfolders

Required file roles

Allowed contents

Forbidden changes

SECTION 1. ROOT LAYOUT
Your backend MUST follow this exact structure:

ONI_System/
    app/
    docs/
    frontend/
    .well-known/
    run.py
    test_ngrok.ps1


Nothing else may be added at the root unless intentionally approved.

SECTION 2. REQUIRED SUBFOLDERS
Inside app/, the required subfolders are:

app/
    main.py
    config.py
    supabase_client.py
    router.py          (if present)
    routes/
    pipelines/
    oni/
    chrono/
    baymax/
    vera/
    victor/
    utils/


These folders are FIXED.
Codex and Claude must NOT create new top-level module folders.
All AI-module logic MUST live in these.

SECTION 3. REQUIRED FILE ROLES
This defines what each folder is responsible for:

app/main.py
    FastAPI app object
    router registration
    CORS settings
    /.well-known mount

app/routes/
    All API route files ONLY
    No business logic here

app/pipelines/
    All pipeline orchestration code
    Pipeline → calls ONI/Baymax/Chrono/Victor/VERA

app/oni/
    Planning, goal selection, reasoning logic for ONI orchestrator

app/baymax/
    Meaning inference, semantics, embeddings

app/chrono/
    Classification, segmentation, timeline calculations

app/vera/
    Validation, error detection, confirmation logic

app/victor/
    Persistent storage utilities, file/log handling

app/utils/
    Shared helpers like gpt_bridge


SECTION 4. ALLOWED CONTENTS
Each folder must contain ONLY its own responsibilities.

Examples:

✔ app/routes/ must contain *_routes.py only
✔ app/pipelines/ must contain pipeline orchestration code only
✔ app/oni/ must contain ONI logic only

NO cross-module mixing.

SECTION 5. FORBIDDEN CHANGES
Codex, Claude, Cursor, GPT must NOT:

• Create a new router folder (like routers/)
• Move pipeline code into routes
• Create new modules outside: oni, chrono, baymax, vera, victor
• Rename prefixes or folder names
• Place business logic inside route files
• Attach pipelines directly to main.py
• Delete or override app/routes/__init__.py
• Add new root folders without explicit user approval