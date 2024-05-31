
def eat_calories(n, m, calories):
    eaten_calories = 0
    current_calories = m

    for i in range(n):
        max_possible_calories = min(current_calories, calories[i])
        eaten_calories += max_possible_calories
        current_calories = (current_calories * 2) // 3

    return eaten_calories

# Input
n, m = map(int, input().split())
calories = list(map(int, input().split()))

# Output
print(eat_calories(n, m, calories))
