
def solve_dice_problem(n, A, dice_values):
    max_possible_sum = sum(dice_values)

    res = []
    for i in range(n):
        min_possible_sum = A - (max_possible_sum - dice_values[i])
        max_possible_sum_without_i = A - dice_values[i]

        num_values_couldnt_show = max(0, min_possible_sum - n + 1, max_possible_sum_without_i - 1)
        res.append(dice_values[i] - num_values_couldnt_show)

    return res


# Input
n, A = map(int, input().split())
dice_values = list(map(int, input().split()))

# Output
output = solve_dice_problem(n, A, dice_values)
print(*output)
```
