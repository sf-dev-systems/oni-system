from fastapi import FastAPI
from .router import api_router

app = FastAPI(title="ONI System")

app.include_router(api_router)


@app.get("/health", tags=["system"])
def health_check():
    return {"status": "ok", "service": "oni-system"}
