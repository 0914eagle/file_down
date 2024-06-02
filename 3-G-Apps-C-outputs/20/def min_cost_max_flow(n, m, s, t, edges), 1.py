
import heapq

def min_cost_max_flow(n, m, s, t, edges):
    graph = [[] for _ in range(n)]
    for u, v, c, w in edges:
        graph[u].append((v, c, w, len(graph[v])))
        graph[v].append((u, 0, -w, len(graph[u])-1))

    flow, cost = 0, 0
    while True:
        dist = [float('inf')] * n
        dist[s] = 0
        prev_edge = [None] * n
        prev_node = [None] * n
        pq = [(0, s)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for i, (v, c, w, rev) in enumerate(graph[u]):
                if c > 0 and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    prev_edge[v] = i
                    prev_node[v] = u
                    heapq.heappush(pq, (dist[v], v))

        if dist[t] == float('inf'):
            break

        f = float('inf')
        v = t
        while v != s:
            u = prev_node[v]
            i = prev_edge[v]
            f = min(f, graph[u][i][1])
            v = u

        flow += f
        cost += f * dist[t]

        v = t
        while v != s:
            u = prev_node[v]
            i = prev_edge[v]
            graph[u][i] = graph[u][i][0], graph[u][i][1] - f, graph[u][i][2], graph[u][i][3]
            graph[v][graph[u][i][3]] = graph[v][graph[u][i][3]][0], graph[v][graph[u][i][3]][1] + f, graph[v][graph[u][i][3]][2], graph[v][graph[u][i][3]][3]
            v = u

    return flow, cost

# Read input
n, m, s, t = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# Solve the problem
max_flow, min_cost = min_cost_max_flow(n, m, s, t, edges)

# Output the result
print(max_flow, min_cost)
