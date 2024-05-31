
def minimal_minutes(N, K, skills):
    teams = [sorted(skills[i:i+K]) for i in range(0, N, K)]
    total_minutes = 0

    for i in range(len(teams)-1):
        for j in range(K):
            if teams[i][j] > teams[i+1][j]:
                total_minutes += 1

    return total_minutes

# Input
N, K = map(int, input().split())
skills = list(map(int, input().split()))

# Output
print(minimal_minutes(N, K, skills))
