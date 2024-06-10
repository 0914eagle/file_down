
from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(graph, source, target):
    pq = [(0, source)]
    dist = defaultdict(lambda: float('inf'))
    dist[source] = 0
    prev = defaultdict(lambda: None)
    while pq:
        d, u = heappop(pq)
        if u == target:
            break
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heappush(pq, (dist[v], v))
    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        curr = prev[curr]
    path.reverse()
    return path

def solve(n, m, p, insecure, connections):
    graph = defaultdict(list)
    for x, y, l in connections:
        graph[x].append((y, l))
        graph[y].append((x, l))
    for i in insecure:
        for j in insecure:
            if i != j:
                if dijkstra(graph, i, j):
                    return "impossible"
    min_cost = 0
    for x, y, l in connections:
        path = dijkstra(graph, x, y)
        if len(path) > 1:
            min_cost += l
    return min_cost

n, m, p = map(int, input().split())
insecure = list(map(int, input().split()))
connections = [tuple(map(int, input().split())) for _ in range(m)]
print(solve(n, m, p, insecure, connections))

