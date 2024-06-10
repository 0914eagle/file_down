

def solve(N, K, M, edges):
    return 0

N, K, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b = map(int, input().split())
    edges.append((a, b))

print(solve(N, K, M, edges))


