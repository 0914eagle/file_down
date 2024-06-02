
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    if not numbers:
        return []
    
    result = [numbers[0]]
    max_num = numbers[0]
    
    for num in numbers[1:]:
        max_num = max(max_num, num)
        result.append(max_num)
    
    return result

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
