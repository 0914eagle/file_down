
from collections import defaultdict

def dfs(node, parent, graph, universities, dist):
    if node in universities:
        dist[node] = 0
    for neighbor in graph[node]:
        if neighbor != parent:
            dfs(neighbor, node, graph, universities, dist)
            dist[node] = max(dist[node], dist[neighbor] + 1)

def solve(n, k, universities, roads):
    graph = defaultdict(list)
    for x, y in roads:
        graph[x].append(y)
        graph[y].append(x)

    dist = {}
    dfs(universities[0], -1, graph, set(universities), dist)

    max_dist = 0
    for u in universities:
        max_dist = max(max_dist, dist[u])

    return 2 * k - max_dist

# Input parsing
n, k = map(int, input().split())
universities = list(map(int, input().split()))
roads = [list(map(int, input().split())) for _ in range(n - 1)]

# Output
print(solve(n, k, universities, roads))
