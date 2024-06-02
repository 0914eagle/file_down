
import heapq

def min_cost_max_flow(n, m, s, t, edges):
    graph = [[] for _ in range(n)]
    for u, v, c, w in edges:
        graph[u].append((v, c, w, len(graph[v])))
        graph[v].append((u, 0, -w, len(graph[u])-1))

    def dijkstra():
        dist = [float('inf')] * n
        dist[s] = 0
        flow = [0] * n
        parent = [-1] * n
        pq = [(0, s)]
        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[u]:
                continue
            for i, (v, c, w, rev) in enumerate(graph[u]):
                if c > 0 and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    parent[v] = (u, i)
                    flow[v] = min(flow[u], c) if flow[u] > 0 else c
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
            v, i = parent[u]
            graph[v][i] = (graph[v][i][0], graph[v][i][1]-flow, graph[v][i][2], graph[v][i][3])
            graph[u][graph[v][i][3]] = (graph[u][graph[v][i][3]][0], graph[u][graph[v][i][3]][1]+flow, graph[u][graph[v][i][3]][2], graph[u][graph[v][i][3]][3])
            u = v

    return max_flow, min_cost

# Input parsing
n, m, s, t = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# Call the function and print the result
result = min_cost_max_flow(n, m, s, t, edges)
print(*result)
