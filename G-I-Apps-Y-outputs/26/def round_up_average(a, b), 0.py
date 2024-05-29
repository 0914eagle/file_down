
import math

def round_up_average(a, b):
    x = (a + b) / 2
    return math.ceil(x)

# Read input
a, b = map(int, input().split())

# Calculate and print result
result = round_up_average(a, b)
print(result)
```
