
from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(graph, start, end):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        cur_dist, cur_node = heappop(pq)
        if cur_node == end:
            return cur_dist
        for neighbor, weight in graph[cur_node]:
            if cur_dist + weight < dist[neighbor]:
                dist[neighbor] = cur_dist + weight
                heappush(pq, (dist[neighbor], neighbor))
    return float('inf')

def solve(n, m, p, insecure, graph):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j and j not in insecure:
                graph[i].append((j, float('inf')))
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                graph[i].append((j, dijkstra(graph, i, j)))

    dist = {node: float('inf') for node in graph}
    dist[1] = 0
    pq = [(0, 1)]
    while pq:
        cur_dist, cur_node = heappop(pq)
        for neighbor, weight in graph[cur_node]:
            if cur_dist + weight < dist[neighbor]:
                dist[neighbor] = cur_dist + weight
                heappush(pq, (dist[neighbor], neighbor))
    return dist[n] if dist[n] < float('inf') else 'impossible'

n, m, p = map(int, input().split())
insecure = set(map(int, input().split()))
graph = defaultdict(list)
for _ in range(m):
    x, y, l = map(int, input().split())
    graph[x].append((y, l))
    graph[y].append((x, l))

print(solve(n, m, p, insecure, graph))

