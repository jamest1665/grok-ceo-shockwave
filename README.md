# GROK-CEO Weekend Shockwave v1.0

**Production-ready foundation** for a hardened autonomous CEO agent.

Built by @Jam3sRyanTaylor + Grok using disciplined engineering practices (inspired by mattpocock/skills: TDD mindset, code review, clean architecture, documentation-first).

## Features (Current — Working End-to-End Demo)

- **Full OODA + Self-Improve cycle** in one cohesive, auditable flow
- **ZeroTrustPolicy** with DRY_RUN enforcement, cost throttling, and Docker sandbox execution
- **Typed extensible state** (Pydantic) with helpers and audit trail
- **Production config** with validation, env overrides, and sensible defaults
- **Structured logging** + immutable audit log
- **CLI** with argparse (`--task`, `--dry-run`)
- **Clean, typed, documented** Python ready for LangGraph upgrade

## Quick Start (Production Path)

```bash
git clone https://github.com/jamest1665/grok-ceo-shockwave.git
cd grok-ceo-shockwave

# Recommended: use uv or pip with pyproject
python -m venv .venv && source .venv/bin/activate
pip install -e "[dev]"          # installs + dev tools (ruff, pytest, mypy)

cp .env.example .env
# edit .env with your XAI_API_KEY (and set DRY_RUN=false when ready)

python run.py --task "Improve audit logging with JSON + trace_id + cost metrics"
```

Or with Docker:

```bash
docker build -t grok-ceo .
docker run --rm -v $(pwd):/app -e DRY_RUN=true grok-ceo
```

## Architecture

```
Config (validated)  →  CEOState (rich model + helpers)
                           ↓
run.py (orchestrator + CLI)
  ├── Observe     (context + metrics)
  ├── Plan        (first-principles + lightweight Digital Twin sim)
  ├── Execute     (ZeroTrust gate + sandboxed action)
  ├── Evaluate    (confidence, risks, history)
  ├── Approve     (threshold or human gate)
  └── Self-Improve (reflect + propose safe upgrades)
                           ↓
Immutable Audit Log + Updated State
```

The demo in `run.py` executes the complete loop and produces real output you can inspect.

## Roadmap to Full Production Agent

1. Replace procedural loop with real `langgraph.StateGraph` + `MemorySaver` checkpointing
2. Add LanceDB for hybrid vector/relational memory (SemanticMemory, EvalHistory, etc.)
3. Implement proper Mesa `Model` + agents for meaningful Digital Twin simulation
4. Wire real LLM calls (langchain-xai) + tool use
5. Expand sandbox to full untrusted code/git execution with input/output validation
6. Add Gradio/FastAPI dashboard for live state, approval UI, and logs
7. Comprehensive test suite + CI (already scaffolded)
8. Packaging, Docker Compose, observability (Prometheus + structured logs)

## Security & Safety
- DRY_RUN=true by default (zero side effects)
- Every mutating action goes through `ZeroTrustPolicy.check()`
- Sandboxed execution (Docker recommended)
- Full immutable audit trail
- No secrets committed; everything via validated config + .env

See `security.md` and the code for implementation details.

**This is a real, working foundation — not hype.** Clone it, run the demo, then iterate with the roadmap above.

Failure is mandatory. Quitting is not.