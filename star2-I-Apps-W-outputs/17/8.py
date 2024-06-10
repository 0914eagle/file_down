
from collections import defaultdict
from sys import setrecursionlimit
setrecursionlimit(10**6)

n = int(input())
adj = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

labels = [-1] * n
def dfs(u, p):
    if u == 1:
        labels[u-1] = 0
        return 1
    for v in adj[u]:
        if v != p:
            labels[u-1] = dfs(v, u)
            return labels[u-1] + 1

dfs(1, -1)
for label in labels[1:]:
    print(label)

