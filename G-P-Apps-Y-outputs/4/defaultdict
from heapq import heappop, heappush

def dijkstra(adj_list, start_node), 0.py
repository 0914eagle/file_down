
import sys
from collections import defaultdict
from heapq import heappop, heappush

def dijkstra(adj_list, start_node):
    n = len(adj_list)
    dist = [float('inf')] * n
    dist[start_node] = 0
    pq = [(0, start_node)]

    while pq:
        cur_dist, cur_node = heappop(pq)
        if cur_dist > dist[cur_node]:
            continue
        for neighbor, weight in adj_list[cur_node]:
            new_dist = cur_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heappush(pq, (new_dist, neighbor))
    
    return dist

def solve(n, m, k, roads, routes):
    adj_list = defaultdict(list)
    for x, y, w in roads:
        adj_list[x-1].append((y-1, w))
        adj_list[y-1].append((x-1, w))
    
    min_total_cost = float('inf')
    for i in range(m):
        saved_cost = roads[i][2]
        roads[i] = (roads[i][0], roads[i][1], 0)
        
        for a, b in routes:
            dist = dijkstra(adj_list, a-1)
            min_total_cost = min(min_total_cost, dist[b-1])
        
        roads[i] = (roads[i][0], roads[i][1], saved_cost)
    
    return min_total_cost

# Input parsing
n, m, k = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(m)]
routes = [list(map(int, input().split())) for _ in range(k)]

# Solving and output
print(solve(n, m, k, roads, routes))
```
