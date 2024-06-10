
from collections import defaultdict

def dfs(node, parent):
    size[node] = 1
    for child in graph[node]:
        if child != parent:
            dfs(child, node)
            size[node] += size[child]

def dfs2(node, parent):
    res[node] = size[node]
    for child in graph[node]:
        if child != parent:
            res[node] = max(res[node], N - size[child])
            dfs2(child, node)

N = int(input())
graph = defaultdict(list)
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
size = [0] * (N + 1)
res = [0] * (N + 1)
dfs(1, 0)
dfs2(1, 0)
print(*res[1:])

