
import heapq

def dijkstra(graph, s, t):
    n = len(graph)
    dist = [float('inf')] * n
    dist[s] = 0
    prev = [-1] * n
    pq = [(0, s)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, c, w in graph[u]:
            if c > 0 and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))

    if dist[t] == float('inf'):
        return None, None

    path = []
    while t != s:
        path.append(t)
        t = prev[t]
    path.append(s)
    path.reverse()

    return dist[t], path

def min_cost_max_flow(n, m, s, t, edges):
    graph = [[] for _ in range(n)]
    for u, v, c, w in edges:
        graph[u].append((v, c, w))
        graph[v].append((u, 0, -w))
    
    flow = 0
    cost = 0
    while True:
        dist, path = dijkstra(graph, s, t)
        if dist is None:
            break
        
        f = float('inf')
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            for edge in graph[u]:
                if edge[0] == v:
                    f = min(f, edge[1])
                    break
        
        flow += f
        cost += f * dist
        
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            for j, (to, c, w) in enumerate(graph[u]):
                if to == v:
                    graph[u][j] = (to, c - f, w)
                    break
            for j, (to, c, w) in enumerate(graph[v]):
                if to == u:
                    graph[v][j] = (to, c + f, w)
                    break
    
    return flow, cost

# Read input
n, m, s, t = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# Solve the problem
max_flow, min_cost = min_cost_max_flow(n, m, s, t, edges)

# Output the result
print(max_flow, min_cost)
