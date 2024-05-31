
import heapq

def min_total_distance(n, m, s, t, warehouses, employees, clients, roads):
    graph = {i: [] for i in range(1, n+1)}
    for u, v, d in roads:
        graph[u].append((v, d))
        graph[v].append((u, d))
    
    warehouse1, warehouse2 = warehouses
    warehouse_distances = {}  # Calculate distances from warehouses to all other intersections
    for warehouse in warehouses:
        dist = [float('inf')] * (n+1)
        dist[warehouse] = 0
        pq = [(0, warehouse)]
        while pq:
            curr_dist, curr_node = heapq.heappop(pq)
            if curr_dist > dist[curr_node]:
                continue
            for neighbor, weight in graph[curr_node]:
                if dist[curr_node] + weight < dist[neighbor]:
                    dist[neighbor] = dist[curr_node] + weight
                    heapq.heappush(pq, (dist[neighbor], neighbor))
        warehouse_distances[warehouse] = dist
    
    # Calculate distances from employees to warehouses and clients
    total_distance = 0
    for employee in employees:
        min_distance = float('inf')
        for client in clients:
            distance = warehouse_distances[warehouse1][employee] + warehouse_distances[warehouse1][client]
            min_distance = min(min_distance, distance)
            distance = warehouse_distances[warehouse2][employee] + warehouse_distances[warehouse2][client]
            min_distance = min(min_distance, distance)
        total_distance += min_distance
    
    return total_distance

# Input parsing
n, m, s, t = map(int, input().split())
warehouses = list(map(int, input().split()))
employees = list(map(int, input().split()))
clients = list(map(int, input().split()))
roads = [list(map(int, input().split())) for _ in range(m)]

# Call the function with the input data
result = min_total_distance(n, m, s, t, warehouses, employees, clients, roads)
print(result)
