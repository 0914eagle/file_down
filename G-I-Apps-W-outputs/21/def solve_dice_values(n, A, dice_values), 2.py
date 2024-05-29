
def solve_dice_values(n, A, dice_values):
    min_possible_sum = n
    max_possible_sum = sum(dice_values)
    
    unable_values = []
    for i in range(len(dice_values)):
        min_dice_sum = A - max_possible_sum + dice_values[i]
        max_dice_sum = A - min_possible_sum + dice_values[i]
        
        unable_values.append(max(min_dice_sum - 1, 0))
    
    return unable_values

# Input
n, A = map(int, input().split())
dice_values = list(map(int, input().split()))

# Output
result = solve_dice_values(n, A, dice_values)
print(*result)
```
