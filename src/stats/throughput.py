from typing import Dict

class ThroughputTracker:
    def __init__(self):
        self.counts_by_provider: Dict[str, int] = {}
        
    def record(self, provider: str) -> None:
        p = provider.lower()
        self.counts_by_provider[p] = self.counts_by_provider.get(p, 0) + 1
        
    def summary(self) -> Dict[str, int]:
        return dict(self.counts_by_provider)
