
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return 0, 1
    
    sum_total = sum(numbers)
    product_total = 1
    for num in numbers:
        product_total *= num
    
    return sum_total, product_total

# Testing the function
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
