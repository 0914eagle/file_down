
import math

def solve_infinite_tetration(N):
    def tetration(a, n):
        if n == 1:
            return a
        return a ** tetration(a, n-1)
    
    def find_a(low, high):
        mid = (low + high) / 2
        if abs(tetration(mid, mid) - N) < 1e-6:
            return mid
        elif tetration(mid, mid) < N:
            return find_a(mid, high)
        else:
            return find_a(low, mid)
    
    return find_a(0, N)

N = float(input())
result = solve_infinite_tetration(N)
print("{:.6f}".format(result))
```
