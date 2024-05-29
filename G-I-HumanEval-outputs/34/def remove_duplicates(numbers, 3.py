
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for idx, num in enumerate(numbers) if num not in numbers[:idx]]

print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
