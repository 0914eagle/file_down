
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    total_sum = sum(numbers) if numbers else 0
    total_product = 1
    for num in numbers:
        total_product *= num
    return total_sum, total_product

# Test cases
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
