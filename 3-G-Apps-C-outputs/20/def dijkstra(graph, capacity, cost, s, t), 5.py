
import heapq

def dijkstra(graph, capacity, cost, s, t):
    n = len(graph)
    dist = [float('inf')] * n
    dist[s] = 0
    flow = [0] * n
    parent = [-1] * n
    pq = [(0, s)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, idx in graph[u]:
            if capacity[(u, v)] > flow[(u, v)] and dist[u] + cost[(u, v)] < dist[v]:
                dist[v] = dist[u] + cost[(u, v)]
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))

    if dist[t] == float('inf'):
        return 0, 0

    f = float('inf')
    c = 0
    v = t
    while parent[v] != -1:
        f = min(f, capacity[(parent[v], v)] - flow[(parent[v], v)])
        c += cost[(parent[v], v)]
        v = parent[v]

    v = t
    while parent[v] != -1:
        flow[(parent[v], v)] += f
        flow[(v, parent[v])] -= f
        v = parent[v]

    return f, f * c

def solve_flow_cost(n, m, s, t, edges):
    graph = [[] for _ in range(n)]
    capacity = {}
    cost = {}

    for u, v, c, w in edges:
        graph[u].append((v, len(graph[v])))
        graph[v].append((u, len(graph[u])))
        capacity[(u, v)] = c
        capacity[(v, u)] = 0
        cost[(u, v)] = w
        cost[(v, u)] = -w

    max_flow = 0
    min_cost = 0
    while True:
        f, c = dijkstra(graph, capacity, cost, s, t)
        if f == 0:
            break
        max_flow += f
        min_cost += c

    return max_flow, min_cost

# Input parsing
n, m, s, t = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# Solve the problem
max_flow, min_cost = solve_flow_cost(n, m, s, t, edges)

# Output the result
print(max_flow, min_cost)
