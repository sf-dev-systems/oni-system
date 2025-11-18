from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.minimal_pipeline_router import router as minimal_router

app = FastAPI(title="ONI Minimal Pipeline API", version="0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(minimal_router)

@app.get("/health")
async def health_check():
    return {"ok": True}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

