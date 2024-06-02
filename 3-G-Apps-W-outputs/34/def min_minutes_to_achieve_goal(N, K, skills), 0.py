
def min_minutes_to_achieve_goal(N, K, skills):
    sorted_skills = sorted(skills)
    minutes = 0
    for i in range(N // K):
        team_skills = sorted_skills[i*K : (i+1)*K]
        for j in range(K):
            if skills[j] != team_skills[j]:
                minutes += 1
    return minutes

# Read input
N, K = map(int, input().split())
skills = list(map(int, input().split()))

# Call the function and print the result
result = min_minutes_to_achieve_goal(N, K, skills)
print(result)
