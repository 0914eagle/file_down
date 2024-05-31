
MOD = 10**9 + 7

def dfs(u, p, color, dist, graph):
    res = 0
    for v in graph[u]:
        if v == p:
            continue
        res = max(res, dfs(v, u, color, dist + 1, graph))
    return res + (color[u] == color) * dist

def solve():
    N = int(input())
    graph = [[] for _ in range(N)]
    color = [0] * N

    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    ans = 0
    ans += dfs(0, -1, 0, 0, graph) % MOD
    ans += dfs(0, -1, 1, 0, graph) % MOD

    print(ans % MOD)

solve()
