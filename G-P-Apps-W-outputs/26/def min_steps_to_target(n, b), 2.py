
def min_steps_to_target(n, b):
    max_steps = 0
    cur_sum = 0
    for i in range(n-1, -1, -1):
        cur_sum += b[i]
        max_steps = max(max_steps, abs(cur_sum))
    return max_steps

# Read input
n = int(input())
b = list(map(int, input().split()))

# Call the function and print the result
print(min_steps_to_target(n, b))
```
