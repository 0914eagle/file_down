
from collections import defaultdict

def dfs(node, graph, visited, path):
visited.add(node)
path.append(node)
for neighbor in graph[node]:
if neighbor not in visited:
dfs(neighbor, graph, visited, path)
return

def find_round_trips(n, roads):
graph = defaultdict(list)
for x, y in roads:
graph[x].append(y)
visited = set()
round_trips = []
for node in range(n):
if node not in visited:
path = []
dfs(node, graph, visited, path)
round_trips.append(path)
return round_trips

def count_new_round_trips(n, m, roads):
round_trips = find_round_trips(n, roads)
new_roads_allowed = 0
for i in range(n):
for j in range(n):
if i != j and all(i not in rt and j not in rt for rt in round_trips):
new_roads_allowed += 1
return new_roads_allowed

n, m = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]
print(count_new_round_trips(n, m, roads))

