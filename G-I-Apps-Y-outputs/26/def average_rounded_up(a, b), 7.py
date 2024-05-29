
import math

def average_rounded_up(a, b):
    x = (a + b) / 2
    return math.ceil(x)

a, b = map(int, input().split())
result = average_rounded_up(a, b)
print(result)
```
