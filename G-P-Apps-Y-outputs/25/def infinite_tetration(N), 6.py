
import math

def infinite_tetration(N):
    # Binary search to find the solution within the range [1/e, e]
    low, high = 1/math.e, math.e
    while high - low > 1e-6:
        mid = (low + high) / 2
        if pow(mid, mid) > N:
            high = mid
        else:
            low = mid
    return low

# Read input
N = float(input().strip())

# Calculate the solution and output the result
result = infinite_tetration(N)
print("{:.6f}".format(result))
```
