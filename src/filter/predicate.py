from typing import List, Dict, Any
from src.core.models import WebhookEvent

def filter_events(events: List[WebhookEvent], key_path: str, expected_val: Any) -> List[WebhookEvent]:
    matched = []
    for e in events:
        val = e.payload.get(key_path)
        if val == expected_val:
            matched.append(e)
    return matched
