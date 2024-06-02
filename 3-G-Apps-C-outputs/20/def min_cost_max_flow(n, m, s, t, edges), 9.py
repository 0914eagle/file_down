
import heapq

def min_cost_max_flow(n, m, s, t, edges):
    graph = [[] for _ in range(n)]
    for u, v, c, w in edges:
        graph[u].append((v, c, w))
        graph[v].append((u, 0, -w))
    
    def dijkstra():
        dist = [float('inf')] * n
        dist[s] = 0
        flow = [0] * n
        cost = [0] * n
        parent = [-1] * n
        pq = [(0, s)]
        
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, c, w in graph[u]:
                if c > 0 and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    parent[v] = u
                    flow[v] = min(flow[u], c) if flow[u] > 0 else c
                    cost[v] = cost[u] + w
                    heapq.heappush(pq, (dist[v], v))
        
        return flow[t], cost[t]
    
    total_flow = 0
    total_cost = 0
    while True:
        flow, cost = dijkstra()
        if flow == 0:
            break
        total_flow += flow
        total_cost += flow * cost
        u = t
        while u != s:
            v = parent[u]
            for i, (x, _, _) in enumerate(graph[v]):
                if x == u:
                    graph[v][i] = (x, 0, 0)
                    break
            for i, (x, _, _) in enumerate(graph[u]):
                if x == v:
                    graph[u][i] = (x, 0, 0)
                    break
            u = v
    
    return total_flow, total_cost

# Input parsing
n, m, s, t = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# Solve the problem
max_flow, min_cost_flow = min_cost_max_flow(n, m, s, t, edges)

# Output the result
print(max_flow, min_cost_flow)
