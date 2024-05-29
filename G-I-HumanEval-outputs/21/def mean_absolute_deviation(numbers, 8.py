
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    mad = sum(abs(x - mean) for x in numbers) / len(numbers)
    return mad


print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output should be 1.0
