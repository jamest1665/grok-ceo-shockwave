from pydantic import BaseModel, Field
from typing import List, Dict

class CEOState(BaseModel):
    context: Dict = Field(default_factory=dict)
    risks: List[str] = Field(default_factory=list)
    costs: Dict = Field(default_factory=lambda: {"usd": 0.0})
    confidence: float = 0.0
    audit_log: List[str] = Field(default_factory=list)