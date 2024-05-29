
import math

def rounded_average(a, b):
    x = (a + b) / 2
    return math.ceil(x)

# Input
a, b = map(int, input().split())

# Output
print(rounded_average(a, b))
```
