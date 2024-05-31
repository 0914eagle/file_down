
def min_minutes_to_achieve_goal(N, K, skills):
    sorted_skills = sorted(skills)
    minutes = 0
    for i in range(N // K):  # Number of teams
        target_skills = sorted_skills[i*K : (i+1)*K]  # Target skills for the team
        team_skills = skills[i*K : (i+1)*K]  # Current skills of the team
        for j in range(K):
            if target_skills[j] != team_skills[j]:
                minutes += 1
    return minutes

# Read input
N, K = map(int, input().split())
skills = list(map(int, input().split()))

# Calculate and print the minimal required number of minutes
print(min_minutes_to_achieve_goal(N, K, skills))
