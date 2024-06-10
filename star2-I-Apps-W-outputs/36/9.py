
from collections import defaultdict
from heapq import heappush, heappop


def dijkstra(graph, source):
    dist = defaultdict(lambda: float('inf'))
    dist[source] = 0
    pq = [(0, source)]
    while pq:
        d, u = heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heappush(pq, (dist[v], v))
    return dist


def solve(n, m, s, t, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
    dist = dijkstra(graph, s)
    for u, v, w in edges:
        if dist[u] + w == dist[v]:
            print('YES')
        elif dist[u] + 1 == dist[v]:
            print('CAN', 1)
        else:
            print('NO')


if __name__ == '__main__':
    n, m, s, t = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    solve(n, m, s, t, edges)

