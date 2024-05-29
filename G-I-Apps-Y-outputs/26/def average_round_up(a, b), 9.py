
import math

def average_round_up(a, b):
    x = (a + b) / 2
    x_rounded = math.ceil(x)
    return x_rounded

a, b = map(int, input().split())
result = average_round_up(a, b)
print(result)
```
