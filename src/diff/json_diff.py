from typing import Dict, Any, Tuple

def compare_payloads(p1: Dict[str, Any], p2: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    added = {k: p2[k] for k in p2 if k not in p1}
    removed = {k: p1[k] for k in p1 if k not in p2}
    return added, removed
