# GROK-CEO Weekend Shockwave v1.0

**Hardened autonomous CEO agent** built by @Jam3sRyanTaylor + Grok. LangGraph-powered OODA loop with Mesa simulation, zero-trust execution, self-improvement, and production foundations.

> **Status**: Foundational skeleton with working end-to-end demo. Core agent loop, state, policy, and audit are functional. Next iterations will wire real LangGraph, LLM calls, LanceDB persistence, and full Mesa Digital Twin.

## Quick Start

```bash
git clone https://github.com/jamest1665/grok-ceo-shockwave.git
cd grok-ceo-shockwave
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # add your XAI_API_KEY etc.
python run.py --task "Refactor the logging system for better auditability and production readiness"
```

- DRY_RUN=True by default (safe, no real git writes or side effects)
- Set `DRY_RUN=false` in .env to enable real (sandboxed) actions

## Architecture (Current v1)

```
Config (pydantic) --> CEOState (Pydantic model)
                     |
                     v
run.py (CLI + OODA Orchestrator)
  |--> Observe (context + metrics)
  |--> Plan (first-principles + simple sim)
  |--> Execute (policy-gated, sandboxed)
  |--> Evaluate (score + risks)
  |--> Approve (threshold or human)
  |--> Self-Improve (propose safe diffs)
                     |
                     v
Audit Log (immutable) + State updates
```

**Components**:
- **ZeroTrustPolicy**: Action whitelisting, cost throttling, DRY_RUN enforcement, Docker sandbox runner (stubbed for demo, real docker-py ready)
- **State**: Typed, extensible Pydantic model with audit trail
- **Demo Loop**: Complete OODA cycle with confidence scoring, risk tracking, and self-reflection

## Features (Implemented in Demo)
- Full OODA cycle with confidence, risks, costs
- Policy-enforced execution (DRY_RUN safe mode)
- Self-improvement proposal (human-confirmed in demo)
- Structured audit logging
- Config-driven (env + defaults)
- Clean, typed, documented code ready for LangGraph upgrade

## Roadmap (Next Logical Steps)
1. Replace demo loop with real LangGraph StateGraph + checkpointing + @node decorators
2. Add LanceDB hybrid memory (EphemeralState, SemanticMemory, EvalHistory)
3. Implement Mesa DigitalTwin with meaningful agent simulation
4. Real LLM integration (langchain-xai or xAI client) + tool calling
5. Full sandbox execution for code/git tools + input/output validation
6. Gradio/FastAPI dashboard for live monitoring + human approval UI
7. Tests, CI (ruff, pytest, secret-scan), Docker Compose, packaging
8. Production hardening: retries (tenacity), structured logging, cost enforcement, observability

## Security Model
- DRY_RUN default (no side effects)
- Policy checks before any mutating action
- Sandboxed execution (Docker or subprocess with limits)
- Audit everything immutably
- No secrets in code; .env + validated config

See security.md for details.

Built iteratively with Grok. Failure is mandatory. Quitting is not.

**Big labs: this is what focused solo + maximally truth-seeking AI can ship.**