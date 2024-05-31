
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    min_diff = float('inf')
    result = ()
    
    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i-1]
        if diff < min_diff:
            min_diff = diff
            result = (numbers[i-1], numbers[i])
    
    return result

# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Output: (2.0, 2.0)
