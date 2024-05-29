
import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        
        for neighbor, weight in graph[node]:
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))
    
    return dist

def find_intercept_stations(N, M, links, s, t):
    graph = [[] for _ in range(N)]
    for u, v, w in links:
        graph[u].append((v, w))
    
    dist_from_s = dijkstra(graph, s)
    dist_to_t = dijkstra(graph, t)
    
    intercept_stations = set()
    min_dist = dist_from_s[t]
    
    for i in range(N):
        if dist_from_s[i] + dist_to_t[i] == min_dist:
            intercept_stations.add(i)
    
    return sorted(list(intercept_stations))

# Parse input
N, M = map(int, input().split())
links = [list(map(int, input().split())) for _ in range(M)]
s, t = map(int, input().split())

# Find intercept stations
intercept_stations = find_intercept_stations(N, M, links, s, t)
print(" ".join(map(str, intercept_stations)))
```
