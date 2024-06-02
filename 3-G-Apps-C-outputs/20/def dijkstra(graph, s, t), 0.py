
import heapq

def dijkstra(graph, s, t):
    n = len(graph)
    dist = [float('inf')] * n
    dist[s] = 0
    pq = [(0, s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, c, w in graph[u]:
            if c > 0 and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    
    return dist[t]

def min_cost_max_flow(n, m, s, t, edges):
    graph = [[] for _ in range(n)]
    for u, v, c, w in edges:
        graph[u].append((v, c, w))
        graph[v].append((u, 0, -w))
    
    flow = 0
    cost = 0
    while True:
        dist = dijkstra(graph, s, t)
        if dist[t] == float('inf'):
            break
        
        f = float('inf')
        v = t
        while v != s:
            u, c, w = min((u, c, w) for u, c, w in graph[v] if dist[u] + w == dist[v])
            f = min(f, c)
            v = u
        
        flow += f
        cost += f * dist[t]
        
        v = t
        while v != s:
            u, c, w = min((u, c, w) for u, c, w in graph[v] if dist[u] + w == dist[v])
            graph[u][graph[u].index((v, c, w))] = (v, c - f, w)
            graph[v][graph[v].index((u, c, -w))] = (u, c + f, -w)
            v = u
    
    return flow, cost

# Read input
n, m, s, t = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# Solve the problem
max_flow, min_cost = min_cost_max_flow(n, m, s, t, edges)

# Output the result
print(max_flow, min_cost)
