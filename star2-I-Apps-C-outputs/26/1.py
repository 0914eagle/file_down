
from collections import defaultdict

def dfs(node, visited, graph):
visited[node] = True
for neighbour in graph[node]:
if not visited[neighbour]:
dfs(neighbour, visited, graph)

def count_round_trips(n, m, roads):
graph = defaultdict(list)
for x, y in roads:
graph[x].append(y)
visited = [False] * n
count = 0
for i in range(n):
if not visited[i]:
dfs(i, visited, graph)
count += 1
return count

n, m = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]
print(count_round_trips(n, m, roads))

