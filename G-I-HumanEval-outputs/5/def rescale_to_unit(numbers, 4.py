
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_num = min(numbers)
    max_num = max(numbers)
    scaled_numbers = [(x - min_num) / (max_num - min_num) for x in numbers]
    return scaled_numbers

# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
