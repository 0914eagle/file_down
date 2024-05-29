
def dfs(graph, visited, v, scores):
    visited[v] = True
    component_score = scores[v]
    for u in graph[v]:
        if not visited[u]:
            component_score += dfs(graph, visited, u, scores)
    return component_score

def maximize_profit(N, M, edges, A, B):
    graph = [[] for _ in range(N)]
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    visited = [False] * N
    profit = 0
    for i in range(N):
        if not visited[i]:
            component_score = dfs(graph, visited, i, B)
            profit = max(profit, component_score)

    total_costs = sum(A)
    return profit - total_costs

# Sample input
N, M = 4, 4
A = [4, 1, 2, 3]
B = [0, 2, -3, 1]
edges = [(1, 2), (2, 3), (3, 4), (4, 2)]

# Sample output
print(maximize_profit(N, M, edges, A, B))
```
