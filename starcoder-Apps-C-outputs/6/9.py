
from queue import PriorityQueue

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    pq = PriorityQueue()
    pq.put((0, start))
    while pq.empty() == False:
        du, u = pq.get()
        for v, w in graph[u]:
            if dist[v] > du + w:
                dist[v] = du + w
                pq.put((dist[v], v))
    return dist

n = int(input())
dist = [[] for _ in range(n)]
for i in range(n):
    p = int(input())
    for _ in range(p):
        l, k, *ds = map(int, input().split())
        dist[i].append((k, l))
        for d in ds:
            dist[i].append((d, 0))
print(min(dijkstra(dist, 0)))
