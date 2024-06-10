

from sys import stdin, stdout
import heapq
from collections import defaultdict


def dijkstra(graph, src):
    dist = defaultdict(lambda: float("inf"))
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, v = heapq.heappop(pq)
        if d > dist[v]:
            continue
        for u, w in graph[v]:
            if dist[u] > dist[v] | w:
                dist[u] = dist[v] | w
                heapq.heappush(pq, (dist[u], u))
    return dist


n, m = map(int, stdin.readline().split())
graph = defaultdict(list)
for i in range(m):
    a, b, w = map(int, stdin.readline().split())
    graph[a].append((b, w))
    graph[b].append((a, w))
q = int(stdin.readline())
for i in range(q):
    s, t = map(int, stdin.readline().split())
    dist = dijkstra(graph, s)
    stdout.write(str(dist[t]) + "\n")

