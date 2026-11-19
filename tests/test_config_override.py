from src.plugins.config_override import DynamicConfigOverride

def test_config_override():
    base = {"timeout": 30, "retries": 3}
    cfg = DynamicConfigOverride(base)
    assert cfg.get("timeout") == 30
    cfg.set_override("timeout", 60)
    assert cfg.get("timeout") == 60
    assert cfg.get("retries") == 3
