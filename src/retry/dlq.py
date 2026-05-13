from typing import List
from src.core.models import WebhookEvent

class DeadLetterQueue:
    def __init__(self):
        self.failed_events: List[WebhookEvent] = []
        
    def push_failed(self, event: WebhookEvent) -> None:
        self.failed_events.append(event)
        
    def pop_all(self) -> List[WebhookEvent]:
        events = list(self.failed_events)
        self.failed_events.clear()
        return events
