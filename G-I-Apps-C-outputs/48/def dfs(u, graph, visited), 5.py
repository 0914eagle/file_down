
def dfs(u, graph, visited):
    visited[u] = True
    component = [u]
    for v in graph[u]:
        if not visited[v]:
            component += dfs(v, graph, visited)
    return component

def max_profit(N, M, A, B, edges):
    graph = {i: [] for i in range(1, N+1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = {i: False for i in range(1, N+1)}
    profits = []
    
    for u in range(1, N+1):
        if not visited[u]:
            component = dfs(u, graph, visited)
            profit = sum([B[i-1] for i in component]) - sum([A[i-1] for i in component])
            profits.append(profit)
    
    return max(profits)

# Input processing
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(M)]

print(max_profit(N, M, A, B, edges))
```
