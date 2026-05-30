import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    APPROVE_THRESHOLD = 0.88
    DRY_RUN = True
    SANDBOX = True
    LLM_MODEL = "grok-4"

config = Config()