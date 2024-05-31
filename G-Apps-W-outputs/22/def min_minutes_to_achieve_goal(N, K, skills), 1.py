
def min_minutes_to_achieve_goal(N, K, skills):
    sorted_skills = sorted(enumerate(skills), key=lambda x: x[1])
    shifts = 0
    for i in range(N//K):
        team_skills = sorted([s[1] for s in sorted_skills[i*K:(i+1)*K]])
        shifts += sum([team_skills[j] != skills[j] for j in range(K)])
    return shifts

# Input parsing
N, K = map(int, input().split())
skills = list(map(int, input().split()))

# Calculate and print the minimal number of minutes required
print(min_minutes_to_achieve_goal(N, K, skills))
