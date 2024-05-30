
import math

def infinite_tetration(N):
    a = 1.0
    while True:
        next_a = math.pow(N, 1.0/a)
        if abs(next_a - a) < 1e-6:
            return next_a
        a = next_a

N = float(input())
result = infinite_tetration(N)
print("{:.6f}".format(result))
```
