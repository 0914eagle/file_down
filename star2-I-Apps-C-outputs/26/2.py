
from collections import defaultdict

def dfs(node, parent):
for child in graph[node]:
if child != parent:
dfs(child, node)

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
x, y = map(int, input().split())
graph[x].append(y)

dfs(0, -1)
print(0)

