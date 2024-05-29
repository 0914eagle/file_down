
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    # To handle the case of an empty list
    if not numbers:
        return 0, 1

    # Initialize the sum and product
    sum_num = 0
    product_num = 1

    # Calculate sum and product
    for num in numbers:
        sum_num += num
        product_num *= num

    return sum_num, product_num

# Test the function
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
