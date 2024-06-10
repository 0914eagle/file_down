
from sys import stdin
from collections import defaultdict

def dfs(u, p, d):
    for v in adj[u]:
        if v != p:
            d[v] = d[u] + 1
            dfs(v, u, d)

n = int(stdin.readline())
adj = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)
d = defaultdict(int)
dfs(1, -1, d)
max_d = max(d.values())
labels = [0] * (max_d + 1)
for u in range(1, n+1):
    for v in adj[u]:
        if d[v] < d[u]:
            v, u = u, v
        labels[d[v] - d[u]] = 1
for i in range(1, max_d+1):
    labels[i] += labels[i-1]
for u in range(1, n+1):
    for v in adj[u]:
        if d[v] < d[u]:
            v, u = u, v
        print(labels[d[v] - d[u]] - 1)

