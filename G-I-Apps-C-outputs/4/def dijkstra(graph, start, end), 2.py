
import heapq

def dijkstra(graph, start, end):
    queue = []
    heapq.heappush(queue, (0, start))
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    while queue:
        cost, current_node = heapq.heappop(queue)

        if current_node == end:
            break

        if cost > dist[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            new_cost = cost + weight
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, neighbor))

    return dist

def find_intercept_station(N, M, links, s, t):
    graph = {i: [] for i in range(N)}
    for u, v, w in links:
        graph[u].append((v, w))

    dist_st = dijkstra(graph, s, t)
    dist_ts = dijkstra(graph, t, s)

    intercept_stations = set()

    for i in range(N):
        if dist_st[i] + dist_ts[i] == dist_st[t] and dist_st[i] != float('inf'):
            intercept_stations.add(i)

    return sorted(list(intercept_stations))

# Input parsing
N, M = map(int, input().split())
links = [list(map(int, input().split())) for _ in range(M)]
s, t = map(int, input().split())

# Calling the function and printing the result
output = find_intercept_station(N, M, links, s, t)
print(*output)
```
