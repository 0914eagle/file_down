
from collections import defaultdict

def solve(n, edges):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    labels = [None] * n
    labels[0] = 0
    def dfs(u, p):
        for v in adj[u]:
            if v == p:
                continue
            labels[v] = 0
            dfs(v, u)
    dfs(1, 0)
    return labels

n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n-1)]
labels = solve(n, edges)
print(*labels, sep='\n')

