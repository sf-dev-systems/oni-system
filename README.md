# ONI System

FastAPI backend for ONI:
- ONI: planner and router
- Baymax: meaning and ontology
- Chrono: structure and segmentation
- VERA: QA and verification
- Dispatcher: pipeline orchestration

## Local setup

1. Create virtualenv

   python -m venv venv
   source venv/bin/activate   # Windows: .\\venv\\Scripts\\activate

2. Install dependencies

   pip install -r requirements.txt

3. Create .env

   copy .env.example to .env and fill in keys.

4. Run server

   uvicorn app.main:app --reload
