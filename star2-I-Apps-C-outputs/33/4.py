
def solve(N, K):
    return 0

N, K = map(int, input().split())
plants = []
for i in range(N):
    X, Y, F = map(int, input().split())
    plants.append((X, Y, F))

energy = solve(N, K)
print(energy)

