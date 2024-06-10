
from collections import defaultdict

def dfs(node, visited):
visited.add(node)
for neighbor in graph[node]:
if neighbor not in visited:
dfs(neighbor, visited)

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
x, y = map(int, input().split())
graph[x].append(y)
visited = set()
dfs(0, visited)
if len(visited) == n:
print(0)
else:
print(1)

