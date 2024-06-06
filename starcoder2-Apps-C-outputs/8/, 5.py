
# 100%
n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)

visited = [False] * n
cycle = False

def dfs(v, parent):
    global cycle
    visited[v] = True
    for u in graph[v]:
        if u == parent:
            continue
        if visited[u]:
            cycle = True
            continue
        dfs(u, v)

for i in range(n):
    if not visited[i]:
        dfs(i, -1)

if cycle:
    print(0)
else:
    print(m // 2)
    for i in range(m):
        print(i + 1)
