
from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_node = heappop(pq)
        if current_node == end:
            return distances[end]
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heappush(pq, (distance, neighbor))
    return float('inf')

def solve(n, m, p, connections, insecure_buildings):
    graph = defaultdict(list)
    for x, y, cost in connections:
        graph[x].append((y, cost))
        graph[y].append((x, cost))
    insecure_buildings = set(insecure_buildings)
    total_cost = 0
    for building in range(1, n + 1):
        if building in insecure_buildings:
            continue
        min_cost = float('inf')
        for insecure_building in insecure_buildings:
            min_cost = min(min_cost, dijkstra(graph, building, insecure_building))
        if min_cost == float('inf'):
            return 'impossible'
        total_cost += min_cost
    return total_cost

n, m, p = map(int, input().split())
insecure_buildings = list(map(int, input().split()))
connections = [tuple(map(int, input().split())) for _ in range(m)]
print(solve(n, m, p, connections, insecure_buildings))

