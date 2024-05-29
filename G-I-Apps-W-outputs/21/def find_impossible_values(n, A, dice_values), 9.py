
def find_impossible_values(n, A, dice_values):
    max_sum = sum(dice_values)
    min_sum = n + (n-1)
    
    possible_values = [min(i+1, d) for i, d in enumerate(dice_values)]
    
    if A < min_sum or A > max_sum:
        return possible_values
    
    diff = A - min_sum
    for i in range(n):
        if diff >= dice_values[i] - 1:
            possible_values[i] = 0
            diff -= dice_values[i] - 1
        else:
            possible_values[i] -= diff
            diff = 0
            break
    
    return possible_values

# Input parsing
n, A = map(int, input().split())
dice_values = list(map(int, input().split()))

# Find and print the result
result = find_impossible_values(n, A, dice_values)
print(*result)
