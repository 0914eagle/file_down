
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    return [val for val in values if isinstance(val, int)]

# Test cases
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
