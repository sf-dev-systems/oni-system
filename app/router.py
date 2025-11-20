from fastapi import APIRouter

from app.routes import test_routes, minimal

api_router = APIRouter()
api_router.include_router(test_routes.router)
api_router.include_router(minimal.router)


@api_router.get("/", tags=["system"])
def root():
    return {"message": "ONI System backend is running"}
