
def max_calories(n, m, calories):
    max_calories = 0
    current_calories = m
    for i in range(n):
        max_calories += min(current_calories, calories[i])
        current_calories = (2 * current_calories) // 3
    return max_calories

# Input
n, m = map(int, input().split())
calories = list(map(int, input().split()))

# Output
print(max_calories(n, m, calories))
