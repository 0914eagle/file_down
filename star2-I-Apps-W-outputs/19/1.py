
from collections import defaultdict

def dfs(node, parent):
    size[node] = 1
    for child in graph[node]:
        if child != parent:
            dfs(child, node)
            size[node] += size[child]

def dfs2(node, parent):
    result[node] = size[node]
    for child in graph[node]:
        if child != parent:
            dfs2(child, node)
            result[node] = max(result[node], N - size[child])

N = int(input())
graph = defaultdict(list)
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
size = [0] * (N + 1)
dfs(1, -1)
result = [0] * (N + 1)
dfs2(1, -1)
print(*result[1:])

