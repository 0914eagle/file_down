
def min_steps_to_target(n, targets):
    steps = 0
    current_sum = 0
    for i in range(n-1, -1, -1):
        target = targets[i]
        diff = target - current_sum
        steps += abs(diff)
        current_sum += diff
    return steps

# Reading input
n = int(input())
targets = list(map(int, input().split()))

# Calling the function and printing the result
print(min_steps_to_target(n, targets))
```
