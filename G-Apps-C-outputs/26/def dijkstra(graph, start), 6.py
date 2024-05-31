
import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]
    
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    
    return dist

def min_total_distance(n, m, s, t, warehouses, employees, clients, roads):
    graph = [[] for _ in range(n)]
    for u, v, d in roads:
        graph[u-1].append((v-1, d))
        graph[v-1].append((u-1, d))
    
    dist_warehouse1, dist_warehouse2 = dijkstra(graph, warehouses[0]-1), dijkstra(graph, warehouses[1]-1)
    
    min_total_dist = float('inf')
    for employee in employees:
        dist = dist_warehouse1[employee-1] if dist_warehouse1[employee-1] < dist_warehouse2[employee-1] else dist_warehouse2[employee-1]
        for client in clients:
            dist += dist_warehouse1[client-1] if dist_warehouse1[client-1] < dist_warehouse2[client-1] else dist_warehouse2[client-1]
            if dist < min_total_dist:
                min_total_dist = dist
    
    return min_total_dist

# Input parsing
n, m, s, t = map(int, input().split())
warehouses = tuple(map(int, input().split()))
employees = list(map(int, input().split()))
clients = list(map(int, input().split()))
roads = [tuple(map(int, input().split())) for _ in range(m)]

# Call the function and print the result
print(min_total_distance(n, m, s, t, warehouses, employees, clients, roads))
