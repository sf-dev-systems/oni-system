from fastapi import FastAPI

from .router import api_router
from app.routes import pipeline as pipeline_routes

app = FastAPI(title="ONI System")

app.include_router(api_router)
app.include_router(pipeline_routes.router)


@app.get("/health", tags=["system"])
def health_check():
    return {"status": "ok", "service": "oni-system"}
