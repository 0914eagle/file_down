
from collections import defaultdict

def dfs(u, parent):
    for v in adj[u]:
        if v != parent:
            dfs(v, u)
            labels[u] |= labels[v]
    labels[u].add(u-1)

n = int(input())
adj = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
labels = defaultdict(set)
dfs(1, 0)
for label in labels[1]:
    print(label)

