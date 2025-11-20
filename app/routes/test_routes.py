from fastapi import APIRouter

router = APIRouter(prefix="/test")


@router.get("/ping")
def ping():
    return {"ping": "pong"}
