
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_val = min(numbers)
    max_val = max(numbers)
    scaled_numbers = [(x - min_val) / (max_val - min_val) for x in numbers]
    return scaled_numbers

# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
