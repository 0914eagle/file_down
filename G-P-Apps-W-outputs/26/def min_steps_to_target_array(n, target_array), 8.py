
def min_steps_to_target_array(n, target_array):
    steps = 0
    current_val = 0
    for i in range(n-1, -1, -1):
        diff = target_array[i] - current_val
        if diff > 0:
            steps += diff
        current_val += diff
    return steps

# Reading input
n = int(input())
target_array = list(map(int, input().split()))

# Calling the function and printing the result
print(min_steps_to_target_array(n, target_array))
```
