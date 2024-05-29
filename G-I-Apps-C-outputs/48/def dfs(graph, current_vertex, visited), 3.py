
def dfs(graph, current_vertex, visited):
    visited[current_vertex] = True
    current_score = 0
    for neighbor in graph[current_vertex]:
        if not visited[neighbor]:
            current_score += dfs(graph, neighbor, visited)
    return vertex_scores[current_vertex] + current_score

def max_profit(N, M, vertex_costs, vertex_scores, edges):
    graph = {i: [] for i in range(1, N + 1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (N + 1)
    max_profit = float('-inf')
    for i in range(1, N + 1):
        if not visited[i]:
            component_score = dfs(graph, i, visited)
            max_profit = max(max_profit, component_score)

    total_vertex_cost = sum(vertex_costs)
    return max_profit - total_vertex_cost

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
U, V = [], []
for _ in range(M):
    u, v = map(int, input().split())
    U.append(u)
    V.append(v)

print(max_profit(N, M, A, B, list(zip(U, V))))
```
