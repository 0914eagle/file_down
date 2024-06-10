
from collections import defaultdict
import heapq

def dijkstra(graph, source):
    dist = defaultdict(lambda: float('inf'))
    dist[source] = 0
    pq = [(0, source)]
    while pq:
        d, v = heapq.heappop(pq)
        if d > dist[v]:
            continue
        for u, w in graph[v]:
            if dist[u] > dist[v] + w:
                dist[u] = dist[v] + w
                heapq.heappush(pq, (dist[u], u))
    return dist

def solve(n, m, s, t, roads):
    graph = defaultdict(list)
    for a, b, l in roads:
        graph[a].append((b, l))
    
    dist = dijkstra(graph, s)
    
    for a, b, l in roads:
        if dist[b] > dist[a] + l:
            return "NO"
    
    for a, b, l in roads:
        if dist[b] == dist[a] + l:
            return "YES"
    
    for a, b, l in roads:
        if dist[b] == dist[a] + l:
            return "CAN", l - dist[b] + dist[a]
    
    return "NO"

n, m, s, t = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(m)]

print(*solve(n, m, s, t, roads))

