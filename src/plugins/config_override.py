from typing import Dict, Any

class DynamicConfigOverride:
    def __init__(self, base_config: Dict[str, Any]):
        self.base = dict(base_config)
        self.overrides: Dict[str, Any] = {}

    def set_override(self, key: str, value: Any) -> None:
        self.overrides[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        if key in self.overrides:
            return self.overrides[key]
        return self.base.get(key, default)
