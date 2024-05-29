
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    sum_res = sum(numbers) if numbers else 0
    prod_res = 1
    for num in numbers:
        prod_res *= num
    return sum_res, prod_res

print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
