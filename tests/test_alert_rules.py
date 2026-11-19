from src.metrics.alert_rules import AlertRuleEvaluator

def test_alert_rules():
    assert AlertRuleEvaluator.evaluate_threshold(10.0, 50.0, 90.0) == "OK"
    assert AlertRuleEvaluator.evaluate_threshold(65.0, 50.0, 90.0) == "WARNING"
    assert AlertRuleEvaluator.evaluate_threshold(95.0, 50.0, 90.0) == "CRITICAL"
