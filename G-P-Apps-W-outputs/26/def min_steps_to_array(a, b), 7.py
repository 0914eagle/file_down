
def min_steps_to_array(a, b):
    diff = 0
    steps = 0
    for i in range(len(a)-1, -1, -1):
        diff += b[i] - a[i]
        steps += abs(diff)
    return steps

# Read input
n = int(input())
b = list(map(int, input().split()))

# Initialize array a with n zeros
a = [0] * n

# Calculate minimum number of steps
result = min_steps_to_array(a, b)
print(result)
```
