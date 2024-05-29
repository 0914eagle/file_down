
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    
    min_number = min(numbers)
    max_number = max(numbers)
    range_values = max_number - min_number
    if range_values == 0:
        return [0.0] * len(numbers)
    return [(num - min_number) / range_values for num in numbers]

# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
