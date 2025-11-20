from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.routes import api_router

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/.well-known", StaticFiles(directory=".well-known"), name="well-known")
app.include_router(api_router)

@app.get("/health", tags=["system"])
def health_check():
    return {"status": "ok", "service": "oni-system"}


@app.post("/pipeline/run", tags=["pipeline"])
def run_pipeline():
    # Placeholder pipeline run endpoint; replace with real pipeline invocation as needed.
    return {"status": "ok", "message": "pipeline started"}
