
def find_impossible_values(n, A, dice_values):
    min_sums = [n - 1] * n
    for i, d in enumerate(dice_values):
        min_sums[i] = A - d + 1

    impossible_values = [0] * n
    for i, d in enumerate(dice_values):
        if A - d < d:
            impossible_values[i] = A - d
        else:
            impossible_values[i] = d - min_sums[i]

    return impossible_values

# Input
n, A = map(int, input().split())
dice_values = list(map(int, input().split()))

# Output
result = find_impossible_values(n, A, dice_values)
print(*result)
```
