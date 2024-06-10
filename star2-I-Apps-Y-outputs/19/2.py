
from sys import stdin
from heapq import heappush, heappop

def dijkstra(graph, start):
    dist = [float('inf')] * len(graph)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, v = heappop(pq)
        if d > dist[v]:
            continue
        for u, w in graph[v]:
            if dist[u] > dist[v] + w:
                dist[u] = dist[v] + w
                heappush(pq, (dist[u], u))
    return dist

n, m, k = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    x, y, w = map(int, stdin.readline().split())
    graph[x - 1].append((y - 1, w))
    graph[y - 1].append((x - 1, w))
routes = []
for _ in range(k):
    a, b = map(int, stdin.readline().split())
    routes.append((a - 1, b - 1))
dist = [dijkstra(graph, i) for i in range(n)]
min_cost = float('inf')
for i in range(n):
    for j in range(i + 1, n):
        if len(graph[i]) < len(graph[j]):
            i, j = j, i
        for w in range(2):
            cost = 0
            for a, b in routes:
                cost += dist[a][b]
            if w == 1:
                cost -= dist[i][j]
            min_cost = min(min_cost, cost)
            if w == 1:
                break
            graph[i].append((j, 0))
            graph[j].append((i, 0))
            dist = [dijkstra(graph, i) for i in range(n)]
            graph[i].pop()
            graph[j].pop()
print(min_cost)

