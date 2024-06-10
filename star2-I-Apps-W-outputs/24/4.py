
from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

graph = defaultdict(list)
for i in range(n-1):
    graph[i+1].append(i+2)
    graph[i+2].append(i+1)

def dfs(v, visited, l, r):
    visited[v] = True
    res = 1
    for u in graph[v]:
        if u not in visited and l <= a[u-1] <= r:
            res += dfs(u, visited, l, r)
    return res

res = 0
for l in range(1, n+1):
    for r in range(l, n+1):
        res += dfs(1, [False]*(n+1), l, r)

print(res)

