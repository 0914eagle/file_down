
import heapq

def dijkstra(N, M, graph, s):
    dist = [float('inf')] * N
    dist[s] = 0
    pq = [(0, s)]

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    return dist

def find_interception_station(N, M, graph, s, t):
    dist_s = dijkstra(N, M, graph, s)
    dist_t = dijkstra(N, M, graph, t)

    shortest_path = dist_s[t]
    intercept_stations = set()

    for u in range(N):
        if dist_s[u] + dist_t[u] == shortest_path:
            intercept_stations.add(u)

    return sorted(intercept_stations)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

s, t = map(int, input().split())

intercept_stations = find_interception_station(N, M, graph, s, t)
print(" ".join(map(str, intercept_stations)))
```
