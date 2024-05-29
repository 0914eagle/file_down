
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    sum_result = 0
    product_result = 1
    
    for num in numbers:
        sum_result += num
        product_result *= num
    
    return sum_result, product_result

# Test cases
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
