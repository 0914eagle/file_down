
from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    min_diff = float('inf')
    closest_pair = ()
    
    for i in range(len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i + 1])
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    
    return closest_pair

# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Output: (2.0, 2.0)
```