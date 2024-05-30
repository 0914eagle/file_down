
import heapq

def dijkstra(adj_list, start):
    n = len(adj_list)
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj_list[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    
    return dist

def solve_berlyatov(n, m, k, roads, routes):
    adj_list = [[] for _ in range(n)]
    for x, y, w in roads:
        adj_list[x-1].append((y-1, w))
        adj_list[y-1].append((x-1, w))

    min_cost = float('inf')
    for i in range(m):
        x, y, w = roads[i]
        adj_list_copy = [lst[:] for lst in adj_list]
        adj_list_copy[x-1].remove((y-1, w))
        adj_list_copy[y-1].remove((x-1, w))

        min_dist = [dijkstra(adj_list_copy, x-1), dijkstra(adj_list_copy, y-1)]
        
        total_cost = 0
        for a, b in routes:
            total_cost += min(min_dist[0][a-1] + min_dist[1][b-1], min_dist[1][a-1] + min_dist[0][b-1])
        
        min_cost = min(min_cost, total_cost)
    
    return min_cost

# Input parsing
n, m, k = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]
routes = [tuple(map(int, input().split())) for _ in range(k)]

# Solve and output
print(solve_berlyatov(n, m, k, roads, routes))
```
