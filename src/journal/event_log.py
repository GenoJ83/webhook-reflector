from typing import List, Optional
from src.core.models import WebhookEvent

class WebhookJournal:
    def __init__(self, capacity: int = 500):
        self.capacity = capacity
        self.events: List[WebhookEvent] = []
        
    def record(self, event: WebhookEvent) -> None:
        if len(self.events) >= self.capacity:
            self.events.pop(0)
        self.events.append(event)
        
    def get_by_id(self, event_id: str) -> Optional[WebhookEvent]:
        for e in self.events:
            if e.id == event_id:
                return e
        return None
        
    def filter_by_provider(self, provider: str) -> List[WebhookEvent]:
        return [e for e in self.events if e.provider.lower() == provider.lower()]
