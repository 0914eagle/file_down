
def maximize_profit(N, M, A, B, edges):
    def dfs(v, component):
        visited[v] = True
        component.append(v)
        for u in graph[v]:
            if not visited[u]:
                dfs(u, component)

    graph = [[] for _ in range(N + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (N + 1)
    profit = 0
    for i in range(1, N + 1):
        if not visited[i]:
            component = []
            dfs(i, component)
            component_score = sum(B[j - 1] for j in component)
            profit += max(component_score, 0)

    return profit - sum(A)

# Sample Input
N, M = 4, 4
A = [4, 1, 2, 3]
B = [0, 2, -3, 1]
edges = [(1, 2), (2, 3), (3, 4), (4, 2)]

print(maximize_profit(N, M, A, B, edges))
```
