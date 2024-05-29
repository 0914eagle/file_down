
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean_val = sum(numbers) / len(numbers)  # Calculate the mean
    mad = sum(abs(x - mean_val) for x in numbers) / len(numbers)  # Calculate MAD
    return mad

# Test the function
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output should be 1.0
