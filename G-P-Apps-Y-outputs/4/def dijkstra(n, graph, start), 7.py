
import sys
from heapq import heappop, heappush

def dijkstra(n, graph, start):
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cost, node = heappop(pq)

        if cost > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            new_cost = dist[node] + weight
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heappush(pq, (new_cost, neighbor))

    return dist

def solve(n, m, k, roads, routes):
    graph = [[] for _ in range(n)]
    for x, y, w in roads:
        graph[x-1].append((y-1, w))
        graph[y-1].append((x-1, w))

    min_total_cost = float('inf')
    for i in range(m):
        x, y, _ = roads[i]
        dist_x = dijkstra(n, graph, x-1)
        dist_y = dijkstra(n, graph, y-1)
        total_cost = 0
        for a, b in routes:
            total_cost += min(dist_x[a-1] + dist_y[b-1], dist_x[b-1] + dist_y[a-1])
        min_total_cost = min(min_total_cost, total_cost)

    return min_total_cost

n, m, k = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(m)]
routes = [tuple(map(int, input().split())) for _ in range(k)]

result = solve(n, m, k, roads, routes)
print(result)
```
