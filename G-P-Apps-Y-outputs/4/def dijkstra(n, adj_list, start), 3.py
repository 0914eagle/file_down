
import heapq

def dijkstra(n, adj_list, start):
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

n, m, k = map(int, input().split())
adj_list = [[] for _ in range(n)]
roads = []
courier_routes = []

for _ in range(m):
    x, y, w = map(int, input().split())
    adj_list[x-1].append((y-1, w))
    adj_list[y-1].append((x-1, w))
    roads.append((x-1, y-1, w))

for _ in range(k):
    a, b = map(int, input().split())
    courier_routes.append((a-1, b-1))

min_total_cost = float('inf')
for i in range(m):
    x, y, _ = roads[i]
    adj_list_copy = [neighbors[:] for neighbors in adj_list]
    adj_list_copy[x].remove((y, roads[i][2]))
    adj_list_copy[y].remove((x, roads[i][2]))
    
    dists = [dijkstra(n, adj_list_copy, start) for start in range(n)]
    
    total_cost = sum(dists[a][b] for a, b in courier_routes)
    min_total_cost = min(min_total_cost, total_cost)

print(min_total_cost)
```
