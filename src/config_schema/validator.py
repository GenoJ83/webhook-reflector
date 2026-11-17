"""Configuration schema validator."""
from typing import Dict, Any, List

def validate_config_keys(config: Dict[str, Any], required_keys: List[str]) -> bool:
    for k in required_keys:
        if k not in config:
            return False
    return True
