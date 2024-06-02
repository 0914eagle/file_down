
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    if not numbers:
        return []

    rolling_max_list = [numbers[0]]
    for i in range(1, len(numbers)):
        rolling_max_list.append(max(rolling_max_list[i-1], numbers[i]))

    return rolling_max_list

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
