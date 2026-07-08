import time
import uuid
from typing import Dict, Any, Optional

class TraceSpan:
    def __init__(self, name: str, trace_id: Optional[str] = None):
        self.name = name
        self.trace_id = trace_id or uuid.uuid4().hex
        self.span_id = uuid.uuid4().hex[:16]
        self.start_time = time.time()
        self.end_time = 0.0
        self.tags: Dict[str, Any] = {}

    def tag(self, key: str, value: Any) -> "TraceSpan":
        self.tags[key] = value
        return self

    def finish(self) -> float:
        self.end_time = time.time()
        return max(0.0, self.end_time - self.start_time)
