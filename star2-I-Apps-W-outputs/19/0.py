
from collections import defaultdict
def dfs(node, parent):
    size[node] = 1
    for child in graph[node]:
        if child != parent:
            dfs(child, node)
            size[node] += size[child]

n = int(input())
graph = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
size = [0] * (n+1)
dfs(1, -1)
result = [0] * (n+1)
for i in range(1, n+1):
    result[size[i]] += 1
print(*result[1:])
