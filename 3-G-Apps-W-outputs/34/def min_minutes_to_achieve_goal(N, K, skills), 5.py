
def min_minutes_to_achieve_goal(N, K, skills):
    teams = [sorted(skills[i:i+K]) for i in range(0, N, K)]
    shifts = 0
    for i in range(1, len(teams)):
        for j in range(K):
            if teams[i][j] < teams[i-1][j]:
                shifts += 1
    return shifts

# Input processing
N, K = map(int, input().split())
skills = list(map(int, input().split()))

# Output
print(min_minutes_to_achieve_goal(N, K, skills))
