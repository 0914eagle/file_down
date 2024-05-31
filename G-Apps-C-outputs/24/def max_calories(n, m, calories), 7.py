
def max_calories(n, m, calories):
    max_calories = 0
    current_calories = m

    for i in range(n):
        max_calories += min(current_calories, calories[i])
        current_calories = current_calories * 2 // 3

    return max_calories

# Input processing
n, m = map(int, input().split())
calories = list(map(int, input().split()))

# Calculate and output the maximum number of calories Stan can consume
print(max_calories(n, m, calories))
