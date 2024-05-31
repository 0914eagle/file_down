
def calculate_max_calories(n, m, courses):
    max_calories = 0
    current_calories = m

    for i in range(n):
        if current_calories == 0:
            break

        max_calories += min(courses[i], current_calories)
        current_calories = min(current_calories * 2 // 3, m)

    return max_calories

# Input processing
n, m = map(int, input().split())
courses = list(map(int, input().split()))

# Calculate and output the maximum calories Stan can consume
print(calculate_max_calories(n, m, courses))
