
import math

def calculate_average_round_up(a, b):
    x = (a + b) / 2
    return math.ceil(x)

a, b = map(int, input().split())
result = calculate_average_round_up(a, b)
print(result)
```
