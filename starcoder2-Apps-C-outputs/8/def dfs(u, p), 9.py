
import sys
sys.setrecursionlimit(10**6)

def dfs(u, p):
    for v in adj[u]:
        if v != p:
            dfs(v, u)
            low[u] = min(low[u], low[v])
            if low[v] > dfn[u]:
                ans.append((u, v))

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

dfn = [-1] * (n + 1)
low = [n + 1] * (n + 1)
cnt = 0
ans = []
for i in range(1, n + 1):
    if dfn[i] == -1:
        dfs(i, -1)

print(len(ans))
for u, v in ans:
    print(u, v)
