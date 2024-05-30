
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
            if dist[u] | w < dist[v]:
                dist[v] = dist[u] | w
                heapq.heappush(pq, (dist[v], v))
    
    return dist

def calculate_transportation_cost(n, m, roads, q, queries):
    adj_list = [[] for _ in range(n)]
    for a, b, w in roads:
        adj_list[a-1].append((b-1, w))
        adj_list[b-1].append((a-1, w))
    
    dist = dijkstra(n, adj_list, 0)
    
    for s, t in queries:
        cost = dist[s-1] | dist[t-1]
        print(cost)

# Input parsing
n, m = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(m)]
q = int(input())
queries = [list(map(int, input().split())) for _ in range(q)]

calculate_transportation_cost(n, m, roads, q, queries)
```
