
def calculate_values(n, A, dice_values):
    max_values = []
    for i in range(n):
        max_value = dice_values[i]
        min_value = A - (sum(dice_values) - max_value)
        values_cannot_show = max_value - min_value
        max_values.append(values_cannot_show)
    
    return max_values

# Input
n, A = map(int, input().split())
dice_values = list(map(int, input().split()))

# Calculate and output the results
result = calculate_values(n, A, dice_values)
print(*result)
```
