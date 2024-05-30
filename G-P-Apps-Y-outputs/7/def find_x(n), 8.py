
import math

def find_x(n):
    x = 1
    while n % 2 == 0:
        n = n // 2
        x *= 2
    return x

t = int(input())
for _ in range(t):
    n = int(input())
    result = find_x(n)
    print(result)
```
