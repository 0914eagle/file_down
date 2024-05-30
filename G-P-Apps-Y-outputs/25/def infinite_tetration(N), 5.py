
import math

def infinite_tetration(N):
    # Binary search to find the value of 'a'
    def find_a(low, high, N):
        while high - low > 1e-6:
            mid = (low + high) / 2
            if math.pow(mid, mid) < N:
                low = mid
            else:
                high = mid
        return low
    
    if N <= 1:
        return N
    
    low = 0
    high = 10
    a = find_a(0, 10, N)
    return a

# Input
N = float(input().strip())

# Output
result = infinite_tetration(N)
print("{:.6f}".format(result))
```
