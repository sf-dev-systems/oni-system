```
docs/module_loading_contract.md
```

This is the document that stops **all import drift, module renaming, pipeline confusion, and code placement errors** across ONI, Baymax, Chrono, VERA, Victor, and utils.

Copy this EXACTLY.

---

# TITLE: ONI System Module Loading Contract

INDEX

1. Purpose
2. Module boundaries
3. Required imports
4. Pipeline loading rules
5. Execution rules
6. Forbidden behavior

---

# SECTION 1. PURPOSE

This contract defines **how modules inside the ONI System must be loaded, imported, and executed**.

Codex, Claude, GPT, Cursor, and all backend code must obey this document to prevent:

• ModuleNotFoundError
• circular imports
• duplicated modules
• refactoring drift
• pipelines calling wrong modules
• logic leaking across modules

This contract enforces **stable module architecture**.

---

# SECTION 2. MODULE BOUNDARIES

The ONI System contains these fixed modules:

```
app/oni/
app/baymax/
app/chrono/
app/vera/
app/victor/
app/pipelines/
app/utils/
```

Each module has one responsibility:

```
oni      → planning, goal selection, orchestration
baymax   → meaning inference, embeddings, semantic reasoning
chrono   → classification, segmentation, timeline processing
vera     → validation and error detection
victor   → storage utilities and persistence
pipelines → orchestrating ONI + Baymax + Chrono + VERA + Victor
utils    → shared helpers only (ex: gpt_bridge)
```

Modules must NEVER absorb responsibilities from other modules.

---

# SECTION 3. REQUIRED IMPORTS

Each module must import others ONLY through allowed paths:

### ✔ Allowed imports:

```
pipelines → may import oni, baymax, chrono, vera, victor
oni       → may import baymax, chrono, vera (but not pipelines)
chrono    → may import baymax
baymax    → may NOT import oni
vera      → may NOT import oni
victor    → may be imported by pipelines only
```

### ❌ Forbidden imports:

```
routes    → may NOT import pipelines or core modules
oni       → may NOT import pipelines
baymax    → may NOT import pipelines
chrono    → may NOT import pipelines
pipelines → may NOT import routes
```

### Rule:

**Pipelines orchestrate modules.
Routes invoke pipelines.
Modules never reach upward.**

---

# SECTION 4. PIPELINE LOADING RULES

A pipeline MUST follow this shape:

```
from app.oni.executive import OniExecutive
from app.baymax.reasoner import BaymaxReasoner
from app.chrono.classifier import ChronoClassifier
from app.vera.validator import VeraValidator
from app.victor.storage import VictorStorage
```

Pipelines MUST:

1. Create instances or call stateless functions from these modules.
2. Combine their outputs.
3. Return a final result for routes.

Pipelines MUST NOT:

• perform routing
• read environment variables
• handle JSON
• write files
• mutate global state

They only orchestrate.

---

# SECTION 5. EXECUTION RULES

### 1. Routes call pipelines ONLY

Example:

```
from app.pipelines.minimal_oni_pipeline import run_minimal_pipeline
```

### 2. Pipelines call ONI, Baymax, Chrono, VERA, Victor

Always in this order:

```
ONI → Baymax → Chrono → VERA → Victor
```

### 3. ONI never calls pipelines

ONI is the orchestrator inside pipelines, not above them.

### 4. No module may initialize a FastAPI app

`app/main.py` is the ONLY file that initializes FastAPI.

### 5. Models must be in `app/pipelines/models` or `app/pipelines/*_models.py`

Never inside ONI, Baymax, Chrono, or VERA folders.

---

# SECTION 6. FORBIDDEN BEHAVIOR

Codex, Claude, GPT, Cursor MUST NOT:

• Move modules between folders
• Rename module folders
• Combine multiple modules into one file
• Create shortcut imports like `import oni`
• Let ONI import pipelines
• Return JSON from a module
• Put FastAPI logic in pipelines
• Put business logic in routes
• Let Victor import ONI
• Let VERA import ONI
• Let baymax import oni
• Let routes import ANY core module directly
• Add global state to ONI, Baymax, Chrono, VERA, Victor

These rules preserve the ONI System architecture.

