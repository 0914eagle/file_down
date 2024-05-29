
from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(graph, start):
    heap = [(0, start, [])]
    visited = set()
    while heap:
        (cost, node, path) = heappop(heap)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == t:
                return path
            for next_node, c in graph[node].items():
                if next_node not in visited:
                    heappush(heap, (cost + c, next_node, path))
    return []

def find_intercept_station(N, M, links, s, t):
    graph = defaultdict(dict)
    for u, v, w in links:
        graph[u][v] = w
    
    shortest_path_s_to_t = dijkstra(graph, s)
    
    intercept_stations = set()
    for node in shortest_path_s_to_t[1:-1]:
        if dijkstra(graph, s)[1:-1] == dijkstra(graph, node)[1:-1] == dijkstra(graph, t)[1:-1]:
            intercept_stations.add(node)
    
    return sorted(list(intercept_stations))

# Input parsing
N, M = map(int, input().split())
links = [list(map(int, input().split())) for _ in range(M)]
s, t = map(int, input().split())

# Find and print intercept stations
intercept_stations = find_intercept_station(N, M, links, s, t)
print(" ".join(map(str, intercept_stations)))
```
