
from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(graph, start):
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        cur_dist, cur_node = heappop(queue)
        for neighbor, weight in graph[cur_node]:
            if cur_dist | weight < distances[neighbor]:
                distances[neighbor] = cur_dist | weight
                heappush(queue, (cur_dist | weight, neighbor))
    return distances


n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))
q = int(input())
for _ in range(q):
    s, t = map(int, input().split())
    distances = dijkstra(graph, s)
    print(distances[t])

