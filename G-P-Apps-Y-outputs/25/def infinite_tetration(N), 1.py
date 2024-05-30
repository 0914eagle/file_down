
import math

def infinite_tetration(N):
    def tetration(a, n):
        if n == 1:
            return a
        return a ** tetration(a, n - 1)
    
    def find_a(N, low, high):
        mid = (low + high) / 2
        result = tetration(mid, mid)
        
        if math.isclose(result, N, abs_tol=1e-5):
            return mid
        elif result < N:
            return find_a(N, mid, high)
        else:
            return find_a(N, low, mid)
    
    return find_a(N, 0.36788, 2.718281)

N = float(input())
result = infinite_tetration(N)
print("{:.6f}".format(result))
```
