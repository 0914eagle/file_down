
from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        curr_dist, curr_node = heappop(pq)
        if curr_dist > distances[curr_node]:
            continue
        for neighbor, weight in graph[curr_node]:
            new_dist = curr_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heappush(pq, (new_dist, neighbor))
    
    return distances

def solve(n, m, s, t, roads):
    graph = defaultdict(list)
    for a, b, l in roads:
        graph[a].append((b, l))
    
    distances = dijkstra(graph, s)
    
    result = []
    for a, b, l in roads:
        if distances[b] == distances[a] + l:
            result.append('YES')
        elif distances[b] < distances[a] + l:
            result.append('CAN {}'.format(l - (distances[b] - distances[a])))
        else:
            result.append('NO')
    
    return result

n, m, s, t = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]
result = solve(n, m, s, t, roads)
print('\n'.join(result))

