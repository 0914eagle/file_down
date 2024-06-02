
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
        for v, cap, cost, rev in graph[u]:
            if cap > 0 and dist[u] + cost < dist[v]:
                dist[v] = dist[u] + cost
                heapq.heappush(pq, (dist[v], v))
    
    return dist[t]

def min_cost_max_flow(n, m, s, t, edges):
    graph = [[] for _ in range(n)]
    for u, v, c, w in edges:
        graph[u].append((v, c, w, len(graph[v])))
        graph[v].append((u, 0, -w, len(graph[u])-1))
    
    flow = 0
    cost = 0
    while True:
        dist = dijkstra(graph, s, t)
        if dist[t] == float('inf'):
            break
        
        f = float('inf')
        v = t
        while v != s:
            u, rev = graph[v][dist[v]]
            f = min(f, graph[u][rev][1])
            v = u
        
        flow += f
        cost += f * dist[t]
        
        v = t
        while v != s:
            u, rev = graph[v][dist[v]]
            graph[u][rev] = (graph[u][rev][0], graph[u][rev][1]-f, graph[u][rev][2], graph[u][rev][3])
            graph[v][dist[v]] = (graph[v][dist[v]][0], graph[v][dist[v]][1]+f, graph[v][dist[v]][2], graph[v][dist[v]][3])
            v = u
    
    return flow, cost

# Read input
n, m, s, t = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# Solve the problem
max_flow, min_cost = min_cost_max_flow(n, m, s, t, edges)

# Output the result
print(max_flow, min_cost)
