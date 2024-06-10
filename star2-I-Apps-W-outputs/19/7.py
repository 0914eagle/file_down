
from collections import defaultdict
def dfs(node, parent):
    for child in graph[node]:
        if child != parent:
            dfs(child, node)
            subtree[node] += subtree[child]

n = int(input())
graph = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
subtree = [1] * (n+1)
dfs(1, -1)
res = [0] * (n+1)
for i in range(1, n+1):
    res[subtree[i]] += 1
print(*res[1:])

