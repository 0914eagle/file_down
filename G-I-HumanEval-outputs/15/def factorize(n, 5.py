
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

print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]

