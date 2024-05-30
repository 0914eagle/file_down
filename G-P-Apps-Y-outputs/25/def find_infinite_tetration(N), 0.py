
import math

def find_infinite_tetration(N):
    if N == 1.0:
        return 1.0

    x = 1.0
    while True:
        y = math.pow(N, 1/x)
        if abs(y - x) < 1e-5:
            return y
        else:
            x = y

# Input
N = float(input())
# Call the function
result = find_infinite_tetration(N)
# Output
print(round(result, 6))
```

