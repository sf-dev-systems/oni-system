# API Route Naming Contract

Purpose  
Defines how ALL endpoints in ONI System must be named.

------------------------------------------------------------

## Route Format

All routes follow EXACT format:

    /{module}/{action}

Examples:
    /minimal/ingest
    /pipeline/run
    /test/ping

------------------------------------------------------------

## Naming Rules

1. No verbs in route *names*
   Allowed: /pipeline/run  
   Not allowed: /analyzeText or /doSomething

2. No snake_case in route segments  
   Correct: /test/ping  
   Wrong: /test/ping_here

3. File names MUST match router variable names  
   minimal_routes.py → minimal_router  
   pipeline_routes.py → pipeline_router

4. Router prefix MUST match module name  
   APIRouter(prefix="/pipeline")  
   APIRouter(prefix="/minimal")

5. Path determines final route  
   prefix="/minimal" + path="/ingest" = /minimal/ingest

------------------------------------------------------------

## Router Aggregator Rules

app/routes/__init__.py MUST contain:

    from .minimal_routes import minimal_router
    from .pipeline_routes import pipeline_router
    from .test_routes import test_router

    api_router = APIRouter()
    api_router.include_router(minimal_router)
    api_router.include_router(pipeline_router)
    api_router.include_router(test_router)

No other imports.  
No other logic.

END