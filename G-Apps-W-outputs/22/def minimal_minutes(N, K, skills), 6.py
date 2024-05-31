
def minimal_minutes(N, K, skills):
    sorted_skills = sorted(enumerate(skills), key=lambda x: x[1])
    shifts = 0
    for i in range(N // K):
        team_skills = sorted(s[1] for s in sorted_skills[i * K: (i + 1) * K])
        shifts += sum(abs(s[1] - t) for s, t in zip(sorted_skills[i * K: (i + 1) * K], team_skills))
    return shifts

# Input
N, K = map(int, input().split())
skills = list(map(int, input().split()))

# Output
print(minimal_minutes(N, K, skills))
