
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

def solve(n, m, k, roads, routes):
    adj_list = [[] for _ in range(n)]
    for x, y, w in roads:
        adj_list[x-1].append((y-1, w))
        adj_list[y-1].append((x-1, w))
    
    all_dist = [dijkstra(adj_list, i) for i in range(n)]
    
    min_total_cost = float('inf')
    for x, y in routes:
        cost = all_dist[x-1][y-1]
        for i in range(n):
            for j, w in adj_list[i]:
                new_cost = cost - all_dist[x-1][y-1] + all_dist[x-1][i] + all_dist[j][y-1]
                min_total_cost = min(min_total_cost, new_cost)
    
    return min_total_cost

n, m, k = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(m)]
routes = [list(map(int, input().split())) for _ in range(k)]

result = solve(n, m, k, roads, routes)
print(result)
```
