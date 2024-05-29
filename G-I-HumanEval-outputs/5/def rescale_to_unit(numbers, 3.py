
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_val = min(numbers)
    max_val = max(numbers)
    if min_val == max_val:
        return [0.0] * len(numbers)
    return [(x - min_val) / (max_val - min_val) for x in numbers]


# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # Output should be [0.0, 0.25, 0.5, 0.75, 1.0]
