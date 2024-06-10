
from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(graph, start, end):
    pq = [(0, start)]
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    while pq:
        curr_dist, curr_node = heappop(pq)
        if curr_node == end:
            return curr_dist
        for neighbor, weight in graph[curr_node]:
            if curr_dist + weight < dist[neighbor]:
                dist[neighbor] = curr_dist + weight
                heappush(pq, (dist[neighbor], neighbor))
    return float('inf')

def solve(n, m, p, insecure_buildings, connections):
    graph = defaultdict(list)
    for x, y, l in connections:
        graph[x].append((y, l))
        graph[y].append((x, l))
    min_cost = float('inf')
    for i in range(1, n+1):
        if i in insecure_buildings:
            continue
        cost = dijkstra(graph, i, insecure_buildings[0])
        if cost == float('inf'):
            continue
        for j in range(1, p):
            cost = min(cost, dijkstra(graph, i, insecure_buildings[j]))
        min_cost = min(min_cost, cost)
    if min_cost == float('inf'):
        return 'impossible'
    return min_cost

n, m, p = map(int, input().split())
insecure_buildings = list(map(int, input().split()))
connections = [tuple(map(int, input().split())) for _ in range(m)]
print(solve(n, m, p, insecure_buildings, connections))

