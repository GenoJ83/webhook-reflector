from src.diff.json_diff import compare_payloads

def test_diff():
    a, r = compare_payloads({"a": 1}, {"a": 1, "b": 2})
    assert a == {"b": 2} and r == {}
