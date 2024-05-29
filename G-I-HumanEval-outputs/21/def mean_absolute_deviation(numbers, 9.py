
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    mad = sum(abs(num - mean) for num in numbers) / len(numbers)
    return mad

# Test the function
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0
