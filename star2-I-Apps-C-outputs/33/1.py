
def solve(N, K, plants):
    return 0

N, K = map(int, input().split())
plants = []
for _ in range(N):
    X, Y, F = map(int, input().split())
    plants.append((X, Y, F))

print(solve(N, K, plants))

