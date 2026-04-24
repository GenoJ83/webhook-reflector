from typing import Dict, Any
import time

def generate_sample_github_push() -> Dict[str, Any]:
    return {
        "ref": "refs/heads/main",
        "before": "0000000000000000000000000000000000000000",
        "after": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
        "repository": {"name": "test-repo", "owner": {"login": "GenoJ83"}},
        "pusher": {"name": "Geno Joshua"}
    }
