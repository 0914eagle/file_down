
import heapq

def shortest_paths(N, M, subway_links, s, t):
    graph = [[] for _ in range(N)]
    for u, v, w in subway_links:
        graph[u].append((v, w))

    def dijkstra(s):
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
    
    dist_from_s = dijkstra(s)
    dist_from_t = dijkstra(t)
    
    intermediate_stations = set()
    for u in range(N):
        if dist_from_s[u] + dist_from_t[u] == dist_from_s[t]:
            intermediate_stations.add(u)
    
    return sorted(intermediate_stations)

# Input parsing
N, M = map(int, input().split())
subway_links = [list(map(int, input().split())) for _ in range(M)]
s, t = map(int, input().split())

# Get output
output = shortest_paths(N, M, subway_links, s, t)
print(" ".join(map(str, output)))
