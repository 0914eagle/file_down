
import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

def min_total_distance(n, m, s, t, warehouses, employees, clients, roads):
    graph = {i: {} for i in range(1, n+1)}
    
    for u, v, d in roads:
        graph[u][v] = d
        graph[v][u] = d
    
    distances_warehouse_a = dijkstra(graph, warehouses[0])
    distances_warehouse_b = dijkstra(graph, warehouses[1])
    
    distances_clients = [dijkstra(graph, client) for client in clients]
    
    min_total_distance = float('infinity')
    
    for employee in employees:
        for i in range(t):
            total_distance = distances_warehouse_a[employee] + distances_clients[i][employee]
            min_total_distance = min(min_total_distance, total_distance)
            
            total_distance = distances_warehouse_b[employee] + distances_clients[i][employee]
            min_total_distance = min(min_total_distance, total_distance)
    
    return min_total_distance

# Input
n, m, s, t = map(int, input().split())
warehouses = list(map(int, input().split()))
employees = list(map(int, input().split()))
clients = list(map(int, input().split()))
roads = [list(map(int, input().split())) for _ in range(m)]

# Output
print(min_total_distance(n, m, s, t, warehouses, employees, clients, roads))
