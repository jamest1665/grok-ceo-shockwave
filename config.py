import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    APPROVE_THRESHOLD = 0.88
    MAX_TOKENS_PER_TICK = 12000
    MAX_USD_PER_TICK = 0.08
    DRY_RUN = True
    SANDBOX = True
    LLM_MODEL = "grok-4"
    GIT_REPO_PATH = "."

config = Config()
os.makedirs("logs", exist_ok=True)