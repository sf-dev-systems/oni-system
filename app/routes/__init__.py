from fastapi import APIRouter

from .pipeline_routes import pipeline_router
from .test_routes import test_router
from .minimal_routes import minimal_router

api_router = APIRouter()
api_router.include_router(pipeline_router)
api_router.include_router(test_router)
api_router.include_router(minimal_router)
