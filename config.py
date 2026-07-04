import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field, field_validator

load_dotenv()

class Config(BaseModel):
    """Production config for GROK-CEO. All values overridable via env."""
    APPROVE_THRESHOLD: float = Field(0.88, ge=0.0, le=1.0, description="Min confidence for auto-approve")
    DRY_RUN: bool = Field(True, description="If True, block all mutating actions (git, exec, file writes)")
    SANDBOX: bool = Field(True, description="Execute untrusted code/tools in isolated Docker container")
    LLM_MODEL: str = Field("grok-4", description="xAI / compatible model name")
    TICK_INTERVAL: int = Field(15, gt=0, description="Proactive tick seconds (future scheduler)")
    MAX_USD_PER_CYCLE: float = Field(0.10, gt=0, description="Hard cost cap per OODA cycle")
    MAX_TOKENS_PER_CYCLE: int = Field(8000, gt=0)
    DB_PATH: str = Field(".lancedb", description="LanceDB persistence dir")
    LOG_PATH: str = Field("logs/audit.log", description="Immutable audit log")
    GIT_REPO_PATH: str = Field(".", description="Target repo for git tools (sandboxed)")
    XAI_API_KEY: str | None = Field(None, description="xAI API key (from env)")

    model_config = {"env_file": ".env", "extra": "ignore"}

    @field_validator("APPROVE_THRESHOLD")
    @classmethod
    def validate_threshold(cls, v):
        if not 0.5 <= v <= 0.95:
            raise ValueError("APPROVE_THRESHOLD should be conservative (0.5-0.95)")
        return v

config = Config()

# Ensure dirs
os.makedirs(os.path.dirname(config.LOG_PATH) or ".", exist_ok=True)
os.makedirs(config.DB_PATH, exist_ok=True)