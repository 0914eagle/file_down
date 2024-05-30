
import math

def infinite_tetration(N):
    if N == 0.0:
        return 0.0
    if N == 1.0:
        return 1.0
    
    def f(a):
        return a ** a

    low, high = 0.0, 2.718281
    mid = 0.0
    while high - low > 1e-6:
        mid = (low + high) / 2
        if f(mid) < N:
            low = mid
        else:
            high = mid
    
    return mid

# Input
N = float(input())

# Output
result = infinite_tetration(N)
print("{:.6f}".format(result))
```
