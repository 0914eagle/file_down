
from collections import defaultdict
import heapq

def dijkstra(graph, start, end):
    pq = [(0, start)]
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    prev = defaultdict(lambda: None)
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        if curr_node == end:
            break
        for neighbor, weight in graph[curr_node]:
            if curr_dist + weight < dist[neighbor]:
                dist[neighbor] = curr_dist + weight
                prev[neighbor] = curr_node
                heapq.heappush(pq, (dist[neighbor], neighbor))
    path = []
    curr = end
    while curr is not None:
        path.append(curr)
        curr = prev[curr]
    path.reverse()
    return path

def solve(n, m, s, t, graph):
    path = dijkstra(graph, s, t)
    result = []
    for i in range(m):
        if graph[i+1][0] in path and graph[i+1][1] in path:
            result.append('YES')
        else:
            if graph[i+1][2] == 1:
                result.append('NO')
            else:
                result.append('CAN {}'.format(graph[i+1][2] - 1))
    return result

n, m, s, t = map(int, input().split())
graph = defaultdict(list)
for i in range(m):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
result = solve(n, m, s, t, graph)
for line in result:
    print(line)

