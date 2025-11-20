Router Checklist

This file defines the correct structure for all FastAPI router files in the ONI System backend. Codex and Claude should follow these rules when creating or modifying routes.

1. Required Files

Every router needs:

A router file inside app/routes/
Example:

app/routes/minimal_routes.py


A router object in that file:

my_router = APIRouter(prefix="/yourprefix")


At least one endpoint:

@my_router.post("/path")


A __init__.py file inside app/routes/ to register routers.

2. Required Router Structure

Each router file must follow this structure:

from fastapi import APIRouter

router_name = APIRouter(prefix="/prefix")

@router_name.get("/path")
async def handler():
    return {...}

3. Required Router Aggregator Structure

File: app/routes/__init__.py

This file must:

Import router objects:

from .pipeline_routes import pipeline_router
from .test_routes import test_router
from .minimal_routes import minimal_router


Create a master router:

api_router = APIRouter()


Register routers:

api_router.include_router(pipeline_router)
api_router.include_router(test_router)
api_router.include_router(minimal_router)


Nothing else should be added to this file.

4. Naming Rules

File name must match import:

minimal_routes.py → from .minimal_routes import minimal_router


Router variable must match include:

minimal_router → api_router.include_router(minimal_router)


Prefix + path determines final route:

prefix="/minimal" + path="/ingest" = /minimal/ingest


Folder must contain __init__.py or router discovery breaks.

5. Test Sequence After Adding Any Router

Restart server:

uvicorn app.main:app --reload


Local test:

Invoke-WebRequest -Uri "http://127.0.0.1:8000/health"


Router test:

Invoke-WebRequest -Uri "http://127.0.0.1:8000/<prefix>/<path>"


Ngrok test:

Invoke-WebRequest -Uri "https://YOUR-NGROK.ngrok-free.dev/<prefix>/<path>"


If all pass, the router is correct.

6. Purpose

This checklist prevents:

• 404 Not Found
• ModuleNotFoundError
• Blank server launches
• Missing router registration
• Incorrect imports

Use this document as the official standard for:
• Codex
• Claude
• GPT
• Cursor
• All ONI backend development