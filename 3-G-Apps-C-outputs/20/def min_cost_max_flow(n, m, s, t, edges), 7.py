
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
        parent = [-1] * n
        pq = [(0, s)]
        
        while pq:
            cost, u = heapq.heappop(pq)
            if cost > dist[u]:
                continue
            for v, c, w in graph[u]:
                if c > 0 and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    flow[v] = min(flow[u], c) if flow[u] > 0 else c
                    parent[v] = u
                    heapq.heappush(pq, (dist[v], v))
        
        return flow[t], dist[t]
    
    max_flow, min_cost = 0, 0
    while True:
        flow, cost = dijkstra()
        if flow == 0:
            break
        max_flow += flow
        min_cost += flow * cost
        u = t
        while u != s:
            v = parent[u]
            for i, (to, c, w) in enumerate(graph[v]):
                if to == u:
                    graph[v][i] = (to, c - flow, w)
                    break
            for i, (to, c, w) in enumerate(graph[u]):
                if to == v:
                    graph[u][i] = (to, c + flow, w)
                    break
            u = v
    
    return max_flow, min_cost

# Read input
n, m, s, t = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# Call the function and print the output
result = min_cost_max_flow(n, m, s, t, edges)
print(*result)
