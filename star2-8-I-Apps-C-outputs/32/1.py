
from collections import defaultdict
from heapq import heappush, heappop
import sys

def dijkstra(start, graph):
    dist = defaultdict(lambda: sys.maxsize)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        cur_dist, cur_node = heappop(pq)
        if cur_dist > dist[cur_node]:
            continue
        for neighbor, weight in graph[cur_node]:
            if cur_dist + weight < dist[neighbor]:
                dist[neighbor] = cur_dist + weight
                heappush(pq, (dist[neighbor], neighbor))
    return dist

n, r = map(int, input().split())
flights = []
for _ in range(r):
    flights.append(tuple(map(int, input().split())))

graph = defaultdict(list)
for a, b, c in flights:
    graph[a].append((b, c))
    graph[b].append((a, c))

dist_from_stockholm = dijkstra(1, graph)

f = int(input())
for _ in range(f):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dist_from_stockholm = dijkstra(1, graph)

total_dist = sys.maxsize
for airport in range(2, n + 1):
    total_dist = min(total_dist, dist_from_stockholm[airport] + dist_from_stockholm[airport])
print(total_dist)

