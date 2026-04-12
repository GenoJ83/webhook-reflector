from src.cli.main import build_parser, main

def test_cli():
    p = build_parser()
    opts = p.parse_args(["--port", "5000", "--forward-to", "http://localhost:8080/events"])
    assert opts.port == 5000
    assert opts.forward_to == "http://localhost:8080/events"
    assert main(["--version"]) == 0
