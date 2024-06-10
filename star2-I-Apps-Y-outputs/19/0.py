
from sys import stdin
from heapq import heappush, heappop

def dijkstra(graph, start, end):
    pq = [(0, start)]
    dist = {start: 0}
    while pq:
        curr_dist, curr_node = heappop(pq)
        if curr_node == end:
            return curr_dist
        for neighbor, weight in graph[curr_node]:
            if neighbor not in dist or curr_dist + weight < dist[neighbor]:
                dist[neighbor] = curr_dist + weight
                heappush(pq, (curr_dist + weight, neighbor))
    return -1

n, m, k = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    x, y, w = map(int, stdin.readline().split())
    graph[x - 1].append((y - 1, w))
    graph[y - 1].append((x - 1, w))
routes = [tuple(map(lambda x: int(x) - 1, stdin.readline().split())) for _ in range(k)]
min_cost = sum(dijkstra(graph, a, b) for a, b in routes)
for i in range(m):
    for j in range(2):
        graph[graph[i][j][0]].remove((i, graph[i][j][1]))
    min_cost = min(min_cost, sum(dijkstra(graph, a, b) for a, b in routes))
    for j in range(2):
        graph[graph[i][j][0]].append((i, graph[i][j][1]))
print(min_cost)

