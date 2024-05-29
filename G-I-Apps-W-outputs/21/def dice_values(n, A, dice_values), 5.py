
def dice_values(n, A, dice_values):
    min_values = [max(0, A - sum(dice_values) + di + 1, 1) for di in dice_values]
    for i in range(n):
        print(min_values[i], end=' ')

# Read input
n, A = map(int, input().split())
dice_values = list(map(int, input().split()))

# Call function
dice_values(n, A, dice_values)
```
