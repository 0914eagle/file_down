
n, m, k = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    x, y, w = map(int, input().split())
    graph[x - 1].append((y - 1, w))
    graph[y - 1].append((x - 1, w))
routes = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(k)]

def dijkstra(start):
    dist = [float('inf')] * n
    dist[start] = 0
    visited = [False] * n
    while True:
        v = -1
        for i in range(n):
            if not visited[i] and (v == -1 or dist[i] < dist[v]):
                v = i
        if v == -1:
            break
        visited[v] = True
        for to, weight in graph[v]:
            if dist[v] + weight < dist[to]:
                dist[to] = dist[v] + weight
    return dist

def solve():
    min_cost = float('inf')
    for i in range(m):
        x, y, w = graph[routes[0][0]][i]
        graph[routes[0][0]][i] = (y, 0)
        dist = dijkstra(routes[0][0])
        cost = sum(dist[b] for a, b in routes)
        min_cost = min(min_cost, cost)
        graph[routes[0][0]][i] = (y, w)
    return min_cost

print(solve())

