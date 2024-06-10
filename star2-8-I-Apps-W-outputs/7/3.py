
from collections import defaultdict

def dfs(graph, vertex, end, path, paths):
if vertex == end:
paths.append(path)
else:
for neighbor in graph[vertex]:
if neighbor not in path:
path.append(neighbor)
dfs(graph, neighbor, end, path, paths)
path.pop()

def count_shortest_paths(graph, start, end):
paths = []
dfs(graph, start, end, [start], paths)
return len(paths)

def solve(vertices, edges, start, end):
graph = defaultdict(list)
for u, v, w in edges:
graph[u].append(v)

return count_shortest_paths(graph, start, end)

vertices, edges = map(int, input().split())
graph = []
for _ in range(edges):
u, v, w = map(int, input().split())
graph.append((u, v, w))

start, end = map(int, input().split())

print(solve(vertices, graph, start, end))

