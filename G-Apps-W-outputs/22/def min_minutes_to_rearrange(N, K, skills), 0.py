
def min_minutes_to_rearrange(N, K, skills):
    skills_sorted = sorted(enumerate(skills), key=lambda x: x[1])

    minutes = 0
    for i in range(N // K):
        team_skills = skills_sorted[i*K: (i+1)*K]
        team_indices = [index for index, _ in team_skills]

        for j, index in enumerate(team_indices):
            minutes += abs(index - i*K - j)

    return minutes

# Input
N, K = map(int, input().split())
skills = list(map(int, input().split()))

# Output
print(min_minutes_to_rearrange(N, K, skills))
