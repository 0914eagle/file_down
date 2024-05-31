
MOD = 10**9 + 7

def dfs(u, p, g, d):
    d[u] = 0
    for v in g[u]:
        if v == p:
            continue
        dfs(v, u, g, d)
        d[u] = max(d[u], d[v] + 1)

def solve(N, edges):
    g = [[] for _ in range(N)]
    for a, b in edges:
        g[a-1].append(b-1)
        g[b-1].append(a-1)

    d = [0] * N
    dfs(0, -1, g, d)

    ans = 0
    for i in range(N):
        ans = (ans + max(d[i], 1)) % MOD

    return ans

# Input
N = int(input())
edges = [list(map(int, input().split())) for _ in range(N-1)]

# Output
print(solve(N, edges))
