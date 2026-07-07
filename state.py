from pydantic import BaseModel, Field
from typing import List, Dict, Any

class CEOState(BaseModel):
    """Core typed state for the GROK-CEO autonomous agent.
    
    Designed for easy migration to LangGraph StateGraph.
    All fields are optional with sensible defaults.
    """
    context: Dict[str, Any] = Field(default_factory=dict, description="Current task/context")
    risks: List[str] = Field(default_factory=list)
    costs: Dict[str, float] = Field(default_factory=lambda: {"usd": 0.0, "tokens": 0})
    priorities: List[str] = Field(default_factory=list)
    confidence: float = Field(0.0, ge=0.0, le=1.0)
    messages: List[Dict[str, Any]] = Field(default_factory=list)
    last_action: str = ""
    digital_twin_snapshot: Dict[str, Any] = Field(default_factory=dict)
    eval_history: List[Dict[str, Any]] = Field(default_factory=list)
    subagent_outputs: Dict[str, Any] = Field(default_factory=dict)
    audit_log: List[str] = Field(default_factory=list)
    iteration: int = 0
    thread_id: str = "grok-ceo-main"
    approved: bool = False

    def add_audit(self, entry: str) -> None:
        """Append to immutable audit log."""
        self.audit_log.append(f"{entry}")

    def update_cost(self, usd: float = 0.0, tokens: int = 0) -> None:
        """Track cumulative cost."""
        self.costs["usd"] = round(self.costs.get("usd", 0) + usd, 4)
        self.costs["tokens"] += tokens

    model_config = {"validate_assignment": True}