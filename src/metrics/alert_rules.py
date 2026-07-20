class AlertRuleEvaluator:
    @staticmethod
    def evaluate_threshold(current_value: float, warning_limit: float, critical_limit: float) -> str:
        if current_value >= critical_limit:
            return "CRITICAL"
        if current_value >= warning_limit:
            return "WARNING"
        return "OK"
