from dataclasses import dataclass, field
from typing import Dict, Any, Optional
import time
import uuid

@dataclass
class WebhookEvent:
    provider: str
    event_type: str
    headers: Dict[str, str]
    payload: Dict[str, Any]
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    received_at: float = field(default_factory=time.time)
    verified: bool = False
