
from collections import defaultdict
from heapq import heappush, heappop
def dijkstra(graph, start):
    dist = defaultdict(lambda: float('inf'))
    prev = defaultdict(lambda: None)
    pq = []
    dist[start] = 0
    heappush(pq, (0, start))
    while pq:
        d, u = heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heappush(pq, (dist[v], v))
    return dist, prev
def find_path(prev, start, end):
    path = []
    at = end
    while at is not None:
        path.append(at)
        at = prev[at]
    return path[::-1]
def solve(n, m, s, t, roads):
    graph = defaultdict(list)
    for a, b, l in roads:
        graph[a].append((b, l))
    dist, prev = dijkstra(graph, s)
    path = find_path(prev, s, t)
    for a, b, l in roads:
        if a in path and b in path:
            print('YES')
        elif a in path and b not in path:
            print('CAN', l - (dist[b] - dist[a]))
        elif a not in path and b in path:
            print('CAN', dist[b] - dist[a])
        else:
            print('NO')

if __name__ == '__main__':
    n, m, s, t = map(int, input().split())
    roads = [tuple(map(int, input().split())) for _ in range(m)]
    solve(n, m, s, t, roads)

