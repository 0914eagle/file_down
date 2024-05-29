
def find_forbidden_values(n, A, dice_values):
    min_possible = n
    max_possible = 0
    
    for i in range(n):
        min_possible += max(0, dice_values[i] - (A - dice_values[i] + 1))
    
    for i in range(n):
        max_possible += min(A - n + 1, dice_values[i])
        
    result = []
    for i in range(n):
        result.append(max(0, A - min_possible - min(dice_values[i], A - n + 1) + 1))
    
    return result

# Input
n, A = map(int, input().split())
dice_values = list(map(int, input().split()))

# Output
result = find_forbidden_values(n, A, dice_values)
print(" ".join(map(str, result)))
```
