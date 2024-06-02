
def minimal_minutes(N, K, skills):
    teams = [sorted(skills[i:i+K]) for i in range(0, N, K)]
    shifts = 0
    for i in range(1, len(teams)):
        shifts += sum(teams[i-1][-j] > teams[i][j] for j in range(K))
    return shifts

# Input
N, K = map(int, input().split())
skills = list(map(int, input().split()))

# Output
print(minimal_minutes(N, K, skills))
