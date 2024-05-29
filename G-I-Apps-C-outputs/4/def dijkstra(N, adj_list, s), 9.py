
import heapq

def dijkstra(N, adj_list, s):
    dist = [float('inf')] * N
    dist[s] = 0
    heap = [(0, s)]
    
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj_list[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    
    return dist

def find_interception_stations(N, M, subway_lines, s, t):
    adj_list = [[] for _ in range(N)]
    for u, v, w in subway_lines:
        adj_list[u].append((v, w))
    
    dist_from_s = dijkstra(N, adj_list, s)
    dist_to_t = dijkstra(N, adj_list, t)
    
    shortest_path_len = dist_from_s[t]
    
    interception_stations = []
    for i in range(N):
        if dist_from_s[i] + dist_to_t[i] == shortest_path_len:
            interception_stations.append(i)
    
    return interception_stations

N, M = map(int, input().split())
subway_lines = [list(map(int, input().split())) for _ in range(M)]
s, t = map(int, input().split())

result = find_interception_stations(N, M, subway_lines, s, t)
print(*result)
```
