
def minimal_minutes(N, K, skills):
    sorted_skills = sorted(skills)
    minutes = 0
    for i in range(N // K):
        team_skills = sorted_skills[i*K : (i+1)*K]
        for j in range(K):
            if skills[j] == team_skills[j]:
                minutes += 1
    return minutes

# Input
N, K = map(int, input().split())
skills = list(map(int, input().split()))

# Output
print(minimal_minutes(N, K, skills))
