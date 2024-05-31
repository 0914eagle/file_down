
def min_minutes(N, K, skill_levels):
    sorted_skills = sorted(skill_levels)
    minutes = 0
    for i in range(N):
        if skill_levels[i] != sorted_skills[i]:
            minutes += 1
    return (minutes + K - 1) // K

# Read input
N, K = map(int, input().split())
skill_levels = list(map(int, input().split()))

# Call the function and print the output
print(min_minutes(N, K, skill_levels))
