
def min_steps_to_target_array(n, target_array):
    steps = 0
    current_sum = 0
    for i in range(n-1, -1, -1):
        current_sum += target_array[i]
        steps = max(steps, abs(current_sum))
    return steps

# Read input
n = int(input())
target_array = list(map(int, input().split()))

# Call the function and print the result
result = min_steps_to_target_array(n, target_array)
print(result)
```
