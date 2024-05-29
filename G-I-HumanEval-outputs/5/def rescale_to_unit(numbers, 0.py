
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_val = min(numbers)
    max_val = max(numbers)
    diff = max_val - min_val
    return [(num - min_val) / diff for num in numbers]

# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
