import pytest
from config import Config, config

def test_config_defaults():
    assert config.APPROVE_THRESHOLD == 0.88
    assert config.DRY_RUN is True
    assert config.SANDBOX is True

def test_config_validation():
    with pytest.raises(ValueError):
        Config(APPROVE_THRESHOLD=0.4)  # too low