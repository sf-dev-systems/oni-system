from fastapi import APIRouter

test_router = APIRouter(prefix="/test")

@test_router.get("/ping")
async def ping():
    return {"status": "ok", "message": "pong"}
