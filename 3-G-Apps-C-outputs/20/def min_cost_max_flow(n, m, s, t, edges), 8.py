
import heapq

def min_cost_max_flow(n, m, s, t, edges):
    graph = [[] for _ in range(n)]
    for u, v, c, w in edges:
        graph[u].append((v, c, w, len(graph[v])))
        graph[v].append((u, 0, -w, len(graph[u])-1))

    def bellman_ford():
        dist = [float('inf')] * n
        dist[s] = 0
        prev_edge = [None] * n
        prev_node = [None] * n
        in_queue = [False] * n
        queue = [s]

        while queue:
            u = queue.pop(0)
            in_queue[u] = False
            for i, (v, c, w, _) in enumerate(graph[u]):
                if c > 0 and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    prev_edge[v] = i
                    prev_node[v] = u
                    if not in_queue[v]:
                        queue.append(v)
                        in_queue[v] = True

        return dist[t], prev_edge, prev_node

    max_flow = 0
    min_cost = 0

    while True:
        cost, prev_edge, prev_node = bellman_ford()
        if dist[t] == float('inf'):
            break

        flow = float('inf')
        v = t
        while v != s:
            u = prev_node[v]
            i = prev_edge[v]
            flow = min(flow, graph[u][i][1])
            v = u

        max_flow += flow
        min_cost += flow * cost

        v = t
        while v != s:
            u = prev_node[v]
            i = prev_edge[v]
            graph[u][i] = (graph[u][i][0], graph[u][i][1] - flow, graph[u][i][2], graph[u][i][3])
            graph[v][graph[u][i][3]] = (graph[v][graph[u][i][3]][0], graph[v][graph[u][i][3]][1] + flow, graph[v][graph[u][i][3]][2], graph[v][graph[u][i][3]][3])
            v = u

    return max_flow, min_cost

# Read input
n, m, s, t = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# Solve problem
max_flow, min_cost = min_cost_max_flow(n, m, s, t, edges)

# Output result
print(max_flow, min_cost)
