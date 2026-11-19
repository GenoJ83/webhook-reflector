from typing import Callable, Dict, List, Any

class PluginHookManager:
    def __init__(self):
        self._hooks: Dict[str, List[Callable]] = {}

    def register(self, hook: str, fn: Callable) -> None:
        self._hooks.setdefault(hook, []).append(fn)

    def trigger(self, hook: str, payload: Any = None) -> Any:
        current = payload
        for fn in self._hooks.get(hook, []):
            current = fn(current)
        return current
