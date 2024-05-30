
import sys
from heapq import heappop, heappush

def dijkstra(graph, start, end):
    pq = [(0, start)]
    dist = [float('inf')] * len(graph)
    dist[start] = 0

    while pq:
        cost, node = heappop(pq)
        if node == end:
            return cost
        if cost > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            if cost + weight < dist[neighbor]:
                dist[neighbor] = cost + weight
                heappush(pq, (dist[neighbor], neighbor))
    
    return float('inf')

N, M = map(int, input().split())
A, B, K, G = map(int, input().split())
G_route = list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B, L = map(int, input().split())
    graph[A].append((B, L))
    graph[B].append((A, L))

min_time = float('inf')
for i in range(G - 1):
    start = G_route[i]
    end = G_route[i + 1]
    time = dijkstra(graph, start, end)
    min_time = min(min_time, time)

delivery_time = min_time + K
print(delivery_time)
```
