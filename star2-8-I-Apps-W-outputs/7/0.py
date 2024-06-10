
from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(graph, source):
heap = [(0, source)]
dist = {source: 0}
prev = {source: None}
while heap:
distance, vertex = heappop(heap)
if vertex not in graph:
continue
for neighbour, weight in graph[vertex].items():
if neighbour in dist:
continue
dist[neighbour] = distance + weight
prev[neighbour] = vertex
heappush(heap, (distance + weight, neighbour))
return dist, prev

def find_shortest_paths(graph, source, destination):
dist, prev = dijkstra(graph, source)
if destination not in dist:
return 0
path_count = {destination: 1}
while destination is not None:
path_count[prev[destination]] = sum(path_count[neighbour] for neighbour in graph[destination])
destination = prev[destination]
return path_count[source]

num_vertices, num_edges = map(int, input().split())
graph = defaultdict(dict)
for _ in range(num_edges):
u, v, w = map(int, input().split())
graph[u][v] = w
source, destination = map(int, input().split())
print(find_shortest_paths(graph, source, destination))

