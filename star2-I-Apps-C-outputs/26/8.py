
from collections import defaultdict

def dfs(u, visited, graph):
visited.add(u)
for v in graph[u]:
if v not in visited:
dfs(v, visited, graph)

def count_round_trips(n, m, roads):
graph = defaultdict(list)
for x, y in roads:
graph[x].append(y)
visited = set()
for u in range(n):
if u not in visited:
dfs(u, visited, graph)
round_trips = len(visited)
return round_trips

n, m = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]
print(count_round_trips(n, m, roads))

