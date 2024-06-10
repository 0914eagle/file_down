
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
res = [max(size[i] for i in range(1, n+1))]
for k in range(2, n+1):
    res.append(max(res[-1], sum(size[i] for i in range(1, n+1) if size[i] >= k)))
print(*res)

