
def min_steps_to_target(n, targets):
    steps = 0
    current_sum = 0

    for i in range(n-1, -1, -1):
        diff = targets[i] - current_sum
        steps += abs(diff)
        current_sum += diff

    return steps

# Input
n = int(input())
targets = list(map(int, input().split()))

# Output
print(min_steps_to_target(n, targets))
```
