from security import policy
from config import config

def test_dry_run_blocks_write():
    original = config.DRY_RUN
    config.DRY_RUN = True
    assert policy.check("git:write", {}) is False
    config.DRY_RUN = original

def test_normal_action_allowed():
    assert policy.check("observe", {}) is True