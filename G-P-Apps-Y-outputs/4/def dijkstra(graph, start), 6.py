
import sys

# Function to find the shortest path using Dijkstra's algorithm
def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    visited = [False] * n

    for _ in range(n):
        min_dist = float('inf')
        min_index = -1

        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                min_index = i

        visited[min_index] = True

        for i in range(n):
            if not visited[i] and graph[min_index][i] != -1:
                if dist[i] > dist[min_index] + graph[min_index][i]:
                    dist[i] = dist[min_index] + graph[min_index][i]

    return dist

def solve(n, m, k, roads, routes):
    graph = [[-1] * n for _ in range(n)]

    for x, y, w in roads:
        graph[x - 1][y - 1] = w
        graph[y - 1][x - 1] = w

    all_routes = []
    for a, b in routes:
        all_routes.append((a - 1, b - 1))

    min_total_cost = float('inf')

    for i in range(m):
        x, y, w = roads[i]
        graph[x - 1][y - 1] = 0
        graph[y - 1][x - 1] = 0

        total_cost = 0
        for a, b in all_routes:
            dist = dijkstra(graph, a)
            total_cost += dist[b]

        min_total_cost = min(min_total_cost, total_cost)

        graph[x - 1][y - 1] = w
        graph[y - 1][x - 1] = w

    return min_total_cost

# Read input
n, m, k = map(int, input().split())
roads = []
for _ in range(m):
    x, y, w = map(int, input().split())
    roads.append((x, y, w))
routes = []
for _ in range(k):
    a, b = map(int, input().split())
    routes.append((a, b))

# Call the solve function and print the result
result = solve(n, m, k, roads, routes)
print(result)
```
