
def min_minutes_to_achieve_goal(N, K, skills):
    sorted_skills = sorted(skills)
    min_minutes = 0
    for i in range(N // K):
        team_skills = sorted_skills[i*K : (i+1)*K]
        min_minutes += sum(team_skills) - K * team_skills[0]
    return min_minutes

# Read input
N, K = map(int, input().split())
skills = list(map(int, input().split()))

# Calculate and print the minimal required number of minutes
print(min_minutes_to_achieve_goal(N, K, skills))
