
from collections import defaultdict

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)] # (distance, node)

    while pq:
        curr_dist, curr_node = heappop(pq)
        if curr_dist > dist[curr_node]: # already visited
            continue

        for neighbor, edge_dist in graph[curr_node]:
            if curr_dist + edge_dist < dist[neighbor]:
                dist[neighbor] = curr_dist + edge_dist
                heappush(pq, (dist[neighbor], neighbor))
    
    return dist

def solve():
    n, m, alpha = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v, c = map(int, input().split())
        graph[u].append((v, c))
        graph[v].append((u, c))
    
    min_dist = float('inf')
    for node in range(1, n+1):
        dist = dijkstra(graph, node)
        min_dist = min(min_dist, max(dist.values())**2 + alpha*m)
    
    return min_dist

print(solve())

