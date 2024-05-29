
import math

def find_average_rounded_up(a, b):
    x = (a + b) / 2
    return math.ceil(x)

if __name__ == "__main__":
    a, b = map(int, input().split())
    result = find_average_rounded_up(a, b)
    print(result)
```
