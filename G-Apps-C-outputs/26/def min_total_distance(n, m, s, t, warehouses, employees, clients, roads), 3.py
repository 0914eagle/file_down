
import heapq

def min_total_distance(n, m, s, t, warehouses, employees, clients, roads):
    graph = {i: {} for i in range(1, n+1)}
    for u, v, d in roads:
        graph[u][v] = d
        graph[v][u] = d
    
    def dijkstra(start):
        distances = {i: float('inf') for i in range(1, n+1)}
        distances[start] = 0
        pq = [(0, start)]
        
        while pq:
            dist, node = heapq.heappop(pq)
            if dist > distances[node]:
                continue
            for neighbor, weight in graph[node].items():
                new_dist = dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
        
        return distances
    
    warehouse_a, warehouse_b = warehouses
    distances_from_a = dijkstra(warehouse_a)
    distances_from_b = dijkstra(warehouse_b)
    
    min_total_distance = float('inf')
    for e in employees:
        for c in clients:
            total_dist = distances_from_a[e] + distances_from_b[c]
            min_total_distance = min(min_total_distance, total_dist)
    
    return min_total_distance

# Input processing
n, m, s, t = map(int, input().split())
warehouses = list(map(int, input().split()))
employees = list(map(int, input().split()))
clients = list(map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(m)]

result = min_total_distance(n, m, s, t, warehouses, employees, clients, roads)
print(result)
