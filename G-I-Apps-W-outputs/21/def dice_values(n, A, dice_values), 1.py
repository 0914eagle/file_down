
def dice_values(n, A, dice_values):
    max_possible_sums = [min(d, A - (n - 1)) for d in dice_values]
    min_possible_sums = [max(1, A - sum(dice_values) + d) for d in dice_values]

    result = [max(0, max_possible_sums[i] - min_possible_sums[i]) for i in range(n)]

    return result


# Input parsing
n, A = map(int, input().split())
dice_values = list(map(int, input().split()))

# Call the function and output the result
result = dice_values(n, A, dice_values)
print(*result)
```
