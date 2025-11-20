from fastapi import APIRouter

pipeline_router = APIRouter(prefix="/pipeline")


@pipeline_router.post("/run")
async def run_pipeline():
    return {"status": "ok", "message": "pipeline started"}


@pipeline_router.get("/run")
async def run_pipeline_info():
    return {"message": "This endpoint requires POST."}
