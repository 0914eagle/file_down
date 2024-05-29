
def calculate_cant_show_values(n, A, dice_values):
    min_values = [max(A - sum(dice_values) + val, 1) for val in dice_values]
    max_values = [min(val, A - n + 1) for val in dice_values]
    for i in range(n):
        print(max(max_values[i] - min_values[i] + 1, 0), end=' ')

# Reading input
n, A = map(int, input().split())
dice_values = list(map(int, input().split()))

# Calling the function
calculate_cant_show_values(n, A, dice_values)
```
