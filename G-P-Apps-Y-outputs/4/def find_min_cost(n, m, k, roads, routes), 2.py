
import sys
input = sys.stdin.readline

def find_min_cost(n, m, k, roads, routes):
    graph = {i: {} for i in range(1, n+1)}
    for x, y, w in roads:
        graph[x][y] = w
        graph[y][x] = w

    dist = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        dist[i][i] = 0
        visited = set()
        stack = [i]
        while stack:
            u = stack.pop()
            visited.add(u)
            for v, w in graph[u].items():
                dist[i][v] = min(dist[i][v], dist[i][u] + w)
                if v not in visited:
                    stack.append(v)

    min_total_cost = float('inf')
    for x, y in routes:
        for i in range(1, n+1):
            for j in range(1, n+1):
                cost = dist[x][i] + dist[i][j] + dist[j][y]
                min_total_cost = min(min_total_cost, cost)
    return min_total_cost

n, m, k = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(m)]
routes = [list(map(int, input().split())) for _ in range(k)]
print(find_min_cost(n, m, k, roads, routes))
```
