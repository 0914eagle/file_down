
from collections import deque

def shortest_paths(N, M, edges, s, t):
    def dijkstra(s):
        dist = [float('inf')] * N
        dist[s] = 0
        pq = [(0, s)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in edges[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        return dist
    
    shortest_path_from_s = dijkstra(s)
    shortest_path_to_t = dijkstra(t)
    middle_stations = set()
    
    for u in range(N):
        if shortest_path_from_s[u] + shortest_path_to_t[u] == shortest_path_from_s[t] and u != s and u != t:
            middle_stations.add(u)
    
    return sorted(list(middle_stations))

# Input processing
N, M = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    edges[u].append((v, w))

s, t = map(int, input().split())

# Output
result = shortest_paths(N, M, edges, s, t)
print(*result)
```
