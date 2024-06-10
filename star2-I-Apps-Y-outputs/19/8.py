
from sys import stdin
from heapq import heappush, heappop

def dijkstra(graph, start):
    dist = [float("inf")] * len(graph)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heappush(pq, (dist[v], v))
    return dist

def solve():
    n, m, k = map(int, stdin.readline().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        x, y, w = map(int, stdin.readline().split())
        graph[x-1].append((y-1, w))
        graph[y-1].append((x-1, w))
    routes = [tuple(map(int, stdin.readline().split())) for _ in range(k)]
    best_cost = float("inf")
    for i in range(m):
        x, y, w = graph[i]
        graph[i] = (x, y, 0)
        cost = sum(dijkstra(graph, a-1)[b-1] for a, b in routes)
        best_cost = min(best_cost, cost)
        graph[i] = (x, y, w)
    return best_cost

print(solve())

