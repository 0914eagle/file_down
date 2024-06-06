
# 2021-06-06 16:12:49
# 2021-06-06 16:31:58

from collections import defaultdict

def dfs(u, parent):
    global visited
    global cycle
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v, u)
        elif v != parent:
            cycle = True

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

cycle = False
visited = [False] * (n + 1)
for u in range(1, n + 1):
    if not visited[u]:
        dfs(u, -1)

if cycle:
    print(m - n + 1)
    for u in range(1, n + 1):
        print(u)
else:
    print(0)
