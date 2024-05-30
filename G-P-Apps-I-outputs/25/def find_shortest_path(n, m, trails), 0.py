
def find_shortest_path(n, m, trails):
    INF = float('inf')
    graph = [[INF for _ in range(n)] for _ in range(n)]
    for u, v, d in trails:
        graph[u][v] = d
    for i in range(n):
        graph[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    return graph[0][n-1]

n, m = map(int, input().split())
trails = [list(map(int, input().split())) for _ in range(m)]

result = find_shortest_path(n, m, trails)
print(result - 12 if result > 12 else 0)
```
