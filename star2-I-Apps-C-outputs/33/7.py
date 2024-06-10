
def solve(N, K):
    pass

N, K = map(int, input().split())
plants = []
for _ in range(N):
    X, Y, F = map(int, input().split())
    plants.append((X, Y, F))

energy, sequence = solve(N, K)
print(energy)
print(len(sequence))
for x, y in sequence:
    print(x, y)

