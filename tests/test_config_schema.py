from src.config_schema.validator import validate_config_keys

def test_config_validation():
    cfg = {"host": "localhost", "port": 8080}
    assert validate_config_keys(cfg, ["host", "port"]) is True
    assert validate_config_keys(cfg, ["host", "missing"]) is False
