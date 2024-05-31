
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    
    numbers.sort()  # Sort the numbers in ascending order
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i+1]) < threshold:
            return True
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
