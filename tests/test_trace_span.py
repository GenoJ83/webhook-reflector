from src.metrics.trace_span import TraceSpan

def test_trace_span():
    span = TraceSpan("db_query")
    span.tag("db.table", "users").tag("db.operation", "SELECT")
    dur = span.finish()
    assert dur >= 0.0
    assert span.tags["db.table"] == "users"
    assert len(span.span_id) == 16
