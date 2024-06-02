
def max_calories(n, m, calories):
    total_calories = 0
    current_calories = m
    for i in range(n):
        if calories[i] <= current_calories:
            total_calories += calories[i]
            current_calories = min(current_calories * 2 // 3, m)
        else:
            break
    return total_calories

# Input
n, m = map(int, input().split())
calories = list(map(int, input().split()))

# Output
print(max_calories(n, m, calories))
