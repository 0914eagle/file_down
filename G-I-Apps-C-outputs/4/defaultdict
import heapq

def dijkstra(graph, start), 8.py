
from collections import defaultdict
import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_dist, current_node = heapq.heappop(queue)
        
        if current_dist > dist[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return dist

def get_intercept_stations(N, M, lines, s, t):
    graph = defaultdict(list)
    for u, v, w in lines:
        graph[u].append((v, w))
    
    dist_s = dijkstra(graph, s)
    dist_t = dijkstra(graph, t)
    
    shortest_path = dist_s[t]
    
    intercept_stations = []
    for u in range(N):
        if u != s and u != t:
            if dist_s[u] + dist_t[u] == shortest_path:
                intercept_stations.append(u)
    
    return intercept_stations

# Read input
N, M = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(M)]
s, t = map(int, input().split())

# Get intercept stations and print output
intercept_stations = get_intercept_stations(N, M, lines, s, t)
print(' '.join(map(str, intercept_stations)))
```
