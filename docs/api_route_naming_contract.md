TITLE: ONI System API Route Naming Contract

INDEX

Purpose

Route prefix rules

Route path rules

Naming rules for router files

Naming rules for router objects

Inclusion rules

Forbidden route patterns

SECTION 1. PURPOSE

This contract defines exact and strict naming rules for all API routes in the ONI System backend.

Codex, Claude, GPT, and Cursor MUST follow these rules to prevent:

• incorrect prefixes
• inconsistent paths
• duplicated routes
• route collisions
• 404 Not Found errors
• wrong router filenames
• broken imports
• api_router drift

This contract ensures all routing remains predictable and stable.

SECTION 2. ROUTE PREFIX RULES

Every router file MUST declare a prefix with APIRouter(prefix="...").

Allowed prefixes:

/minimal
/pipeline
/test
/oni
/chrono
/baymax
/vera
/victor


Prefixes MUST:

• be lowercase
• use only one word
• match the module they represent
• match the router filename
• never contain uppercase letters
• never contain slashes (except the leading /)

Example:

minimal_routes.py → prefix="/minimal"
pipeline_routes.py → prefix="/pipeline"

SECTION 3. ROUTE PATH RULES

Inside each router, all endpoint paths MUST:

• start with "/"
• use lowercase
• use hyphens ONLY when needed
• be short and descriptive

Allowed verbs:

/run
/ingest
/ping
/validate
/classify
/analyze
/store


Examples:

@router.post("/run")
@router.get("/ping")
@router.post("/ingest")


Final route = prefix + path:

prefix="/minimal" + path="/ingest" = /minimal/ingest

SECTION 4. NAMING RULES FOR ROUTER FILES

Every router file MUST follow this naming pattern:

<prefix>_routes.py


Examples:

minimal_routes.py
pipeline_routes.py
test_routes.py
oni_routes.py
chrono_routes.py
baymax_routes.py
vera_routes.py
victor_routes.py


Forbidden:

minimal.py
router_minimal.py
routes_minimal.py
xrouter.py

SECTION 5. NAMING RULES FOR ROUTER OBJECTS

Inside each router file, the router variable MUST be named:

<prefix>_router


Examples:

minimal_router = APIRouter(prefix="/minimal")
pipeline_router = APIRouter(prefix="/pipeline")


Forbidden:

router = ...
r = ...
api = ...
main_router = ...

SECTION 6. INCLUSION RULES

Inside app/routes/__init__.py:

api_router.include_router(minimal_router)
api_router.include_router(pipeline_router)
api_router.include_router(test_router)
api_router.include_router(oni_router)
api_router.include_router(chrono_router)
api_router.include_router(baymax_router)
api_router.include_router(vera_router)
api_router.include_router(victor_router)


Rules:

✔ MUST include all routers
✔ MUST follow alphabetical or logical order
✔ MUST match prefix and router variable name
✔ MUST NOT include routers twice
✔ MUST NOT omit active modules

SECTION 7. FORBIDDEN ROUTE PATTERNS

Codex, Claude, GPT, Cursor MUST NOT:

• create routes without prefixes
• create routes directly under /
• create nested prefixes like /minimal/v1/ingest
• use camelCase or PascalCase
• use uppercase letters in paths
• define two identical routes in different files
• autodetect routes based on filename
• create new folders named routers, api, or endpoints
• rename any existing routes without approval

This keeps the routing tree stable.
