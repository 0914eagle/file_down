
from collections import deque

def dijkstra(graph, src):
    dist = [float('inf') for _ in range(N)]
    dist[src] = 0
    prev = [-1 for _ in range(N)]
    
    pq = [(0, src)]
    while pq:
        dist_u, u = heapq.heappop(pq)
        for v, w in graph[u]:
            if dist_u + w < dist[v]:
                dist[v] = dist_u + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    return dist, prev
    
def find_cycle(graph, src, dist, prev):
    for v, w in graph[src]:
        if dist[v] == 0 and v != src:
            return [v, src]
    
    curr = src
    while prev[curr] != -1:
        curr = prev[curr]
        if curr == src:
            return [curr, prev[curr]]
    return None
    
N, M, alpha = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v, c = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append((v, c))
    graph[v].append((u, c))
    
dist, prev = dijkstra(graph, 0)
if dist[-1] == float('inf'):
    print('Poor girl')
else:
    cycle = find_cycle(graph, 0, dist, prev)
    
    total_candies = 0
    for u, v in zip(cycle, cycle[1:]):
        for v_, c in graph[u]:
            if v_ == v:
                total_candies = max(total_candies, c)
    
    print(total_candies**2 + alpha * len(cycle))

