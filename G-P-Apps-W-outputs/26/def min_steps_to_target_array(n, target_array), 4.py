
def min_steps_to_target_array(n, target_array):
    current_sum = 0
    max_diff = 0
    
    for i in range(n):
        current_sum += target_array[i]
        max_diff = max(max_diff, abs(current_sum))
    
    return max_diff

# Input reading
n = int(input())
target_array = list(map(int, input().split()))

# Output
print(min_steps_to_target_array(n, target_array))
```
