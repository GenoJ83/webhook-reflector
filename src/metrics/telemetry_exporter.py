from typing import Dict

class TelemetryCollector:
    def __init__(self):
        self.counters: Dict[str, int] = {}
        self.gauges: Dict[str, float] = {}

    def increment(self, metric: str, value: int = 1) -> None:
        self.counters[metric] = self.counters.get(metric, 0) + value

    def set_gauge(self, metric: str, value: float) -> None:
        self.gauges[metric] = value

    def to_prometheus(self) -> str:
        lines = []
        for k, v in sorted(self.counters.items()):
            lines.append(f"# TYPE {k} counter\n{k} {v}")
        for k, v in sorted(self.gauges.items()):
            lines.append(f"# TYPE {k} gauge\n{k} {v}")
        return "\n".join(lines)
