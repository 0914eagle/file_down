
def min_minutes_to_achieve_goal(N, K, skills):
    min_minutes = 0
    for i in range(N // K):
        team_skills = skills[i*K : (i+1)*K]
        sorted_team_skills = sorted(team_skills)
        for j in range(K):
            if team_skills[j] != sorted_team_skills[j]:
                min_minutes += 1
    return min_minutes

# Input processing
N, K = map(int, input().split())
skills = list(map(int, input().split()))

# Call the function and print the result
result = min_minutes_to_achieve_goal(N, K, skills)
print(result)
