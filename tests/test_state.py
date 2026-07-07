from state import CEOState

def test_state_creation():
    state = CEOState(context={"task": "test"})
    assert state.confidence == 0.0
    assert state.iteration == 0
    state.add_audit("test entry")
    assert len(state.audit_log) == 1

def test_cost_update():
    state = CEOState()
    state.update_cost(usd=0.05, tokens=100)
    assert state.costs["usd"] == 0.05