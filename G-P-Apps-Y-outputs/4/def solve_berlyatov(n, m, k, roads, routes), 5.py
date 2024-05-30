
def solve_berlyatov(n, m, k, roads, routes):
    graph = {}
    for i in range(1, n + 1):
        graph[i] = {}
    
    for x, y, w in roads:
        graph[x][y] = w
        graph[y][x] = w
    
    dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0
        for j in graph[i]:
            dist[i][j] = graph[i][j]
            dist[j][i] = graph[i][j]
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    min_cost = float('inf')
    for i in range(1, m + 1):
        x, y, w = roads[i-1]
        min_cost = min(min_cost, dist[x][y] + w)
    
    for a, b in routes:
        min_cost = min(min_cost, dist[a][b])
    
    return min_cost

# Input parsing
n, m, k = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(m)]
routes = [list(map(int, input().split())) for _ in range(k)]

result = solve_berlyatov(n, m, k, roads, routes)
print(result)
```
