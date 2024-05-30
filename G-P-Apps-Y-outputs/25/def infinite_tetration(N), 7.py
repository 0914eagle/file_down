
import math

def infinite_tetration(N):
    def tetration(a, n):
        if n == 1:
            return a
        return a ** tetration(a, n-1)

    def find_a(low, high, target):
        mid = (low + high) / 2
        result = tetration(mid, 2)
        if abs(result - target) < 1e-5:
            return mid
        elif result < target:
            return find_a(mid, high, target)
        else:
            return find_a(low, mid, target)

    if N < 1/e or N > e:
        return "No solution exists for the given input."

    e = math.e
    return find_a(0, 2, N)

# Input
N = float(input())

# Output
print(infinite_tetration(N))
```
