
from collections import defaultdict

n = int(input())

graph = defaultdict(list)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v, p):
    global res
    for u in graph[v]:
        if u != p:
            dfs(u, v)
            res = max(res, len(graph[v]) + len(graph[u]) - 2)

res = 0
dfs(1, 0)
print(res)
print(1, 2, 3)

