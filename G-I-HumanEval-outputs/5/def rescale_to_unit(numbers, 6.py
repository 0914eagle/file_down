
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements.")
    
    min_num = min(numbers)
    max_num = max(numbers)
    
    if min_num == max_num:
        return [0.0] * len(numbers)
    
    rescaled = [(num - min_num) / (max_num - min_num) for num in numbers]
    
    return rescaled

# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit([1.0, 1.0, 1.0]))  # Output: [0.0, 0.0, 0.0]
print(rescale_to_unit([-2.0, 0.0, 2.0]))  # Output: [0.0, 0.5, 1.0]
