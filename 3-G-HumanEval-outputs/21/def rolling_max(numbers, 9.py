
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    if not numbers:
        return []

    max_values = [numbers[0]]
    for i in range(1, len(numbers)):
        max_values.append(max(max_values[i - 1], numbers[i]))

    return max_values

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
