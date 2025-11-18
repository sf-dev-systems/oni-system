from fastapi import APIRouter

api_router = APIRouter()

@api_router.get("/", tags=["system"])
def root():
    return {"message": "ONI System backend is running"}
