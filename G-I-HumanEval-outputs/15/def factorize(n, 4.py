
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1

    return factors

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
