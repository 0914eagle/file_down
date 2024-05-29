
from collections import defaultdict
import heapq

def dijkstra(graph, start):
    heap = [(0, start)]
    visited = set()
    shortest_paths = {node: float('inf') for node in graph}
    shortest_paths[start] = 0
    
    while heap:
        (current_distance, current_node) = heapq.heappop(heap)
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    
    return shortest_paths

def find_intercepting_stations(N, M, lines, s, t):
    graph = defaultdict(dict)
    
    for u, v, w in lines:
        if v not in graph[u] or w < graph[u][v]:
            graph[u][v] = w
    
    s_distances = dijkstra(graph, s)
    t_distances = dijkstra(graph, t)
    
    intercepting_stations = [u for u in graph if s_distances[u] + t_distances[u] == s_distances[t]]
    intercepting_stations.sort()
    
    return intercepting_stations

# Input parsing
N, M = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(M)]
s, t = map(int, input().split())

# Find and output intercepting stations
result = find_intercepting_stations(N, M, lines, s, t)
print(' '.join(map(str, result)))
```
