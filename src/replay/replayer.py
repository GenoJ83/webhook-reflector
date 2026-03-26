from typing import Dict, Any, Callable
from src.core.models import WebhookEvent

class WebhookReplayer:
    def __init__(self, forward_handler: Callable[[WebhookEvent], bool] = None):
        self.handler = forward_handler or (lambda e: True)
        
    def replay(self, event: WebhookEvent) -> bool:
        return self.handler(event)
