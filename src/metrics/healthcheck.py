from typing import Dict

class ComponentHealthCheck:
    def __init__(self):
        self.checks: Dict[str, bool] = {}

    def register_check(self, component: str, is_healthy: bool) -> None:
        self.checks[component] = is_healthy

    def get_aggregate_status(self) -> str:
        if not self.checks:
            return "HEALTHY"
        if all(self.checks.values()):
            return "HEALTHY"
        if any(self.checks.values()):
            return "DEGRADED"
        return "UNHEALTHY"
