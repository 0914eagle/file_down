
from math import factorial

def count_round_dances(n):
    return factorial(n-1) // (2**(n//2))

n = int(input())
print(count_round_dances(n))
```
