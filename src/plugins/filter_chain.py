from typing import Callable, List, Any

class FilterChain:
    def __init__(self):
        self.filters: List[Callable[[Any], Any]] = []

    def add_filter(self, filter_fn: Callable[[Any], Any]) -> "FilterChain":
        self.filters.append(filter_fn)
        return self

    def execute(self, initial_data: Any) -> Any:
        data = initial_data
        for f in self.filters:
            data = f(data)
        return data
