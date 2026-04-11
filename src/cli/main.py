import argparse

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="webhookreflector", description="Local webhook tunnel and verifier")
    p.add_argument("--version", action="store_true", help="Print version")
    p.add_argument("--port", type=int, default=4000, help="Listen port")
    p.add_argument("--secret", help="HMAC verification secret")
    p.add_argument("--forward-to", default="http://localhost:3000/webhook", help="Forward destination URL")
    return p

def main(args=None):
    p = build_parser()
    opts = p.parse_args(args)
    if opts.version:
        print("webhookreflector v0.1.0")
        return 0
    return 0
