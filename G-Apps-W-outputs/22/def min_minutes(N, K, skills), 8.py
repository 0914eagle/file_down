
def min_minutes(N, K, skills):
    teams = [sorted(skills[i:i+K]) for i in range(0, N, K)]
    shifts = 0
    for team in teams:
        shifts += sum(abs(team[i] - team[K//2]) for i in range(K))

    return shifts

# Input processing
N, K = map(int, input().split())
skills = list(map(int, input().split()))

result = min_minutes(N, K, skills)
print(result)
