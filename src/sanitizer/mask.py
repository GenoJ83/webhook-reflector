from typing import Dict, Any

SENSITIVE_KEYS = ["token", "secret", "password", "authorization", "api_key"]

def mask_sensitive_fields(payload: Dict[str, Any]) -> Dict[str, Any]:
    out = dict(payload)
    for k, v in out.items():
        if any(s in k.lower() for s in SENSITIVE_KEYS):
            out[k] = "********"
    return out
