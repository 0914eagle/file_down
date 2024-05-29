
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    if not numbers:
        return 0.0
    
    mean = sum(numbers) / len(numbers)
    
    deviation_sum = sum(abs(x - mean) for x in numbers)
    mean_absolute_deviation = deviation_sum / len(numbers)
    
    return mean_absolute_deviation

# Test case
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0
