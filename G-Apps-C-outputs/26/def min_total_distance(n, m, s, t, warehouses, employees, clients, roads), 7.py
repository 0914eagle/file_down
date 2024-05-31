
import heapq

def min_total_distance(n, m, s, t, warehouses, employees, clients, roads):
    graph = {i: [] for i in range(1, n+1)}
    for u, v, d in roads:
        graph[u].append((v, d))
        graph[v].append((u, d))
    
    warehouse_distances = {i: 0 for i in range(1, n+1)}
    for warehouse in warehouses:
        visited = set()
        queue = [(0, warehouse)]
        while queue:
            dist, node = heapq.heappop(queue)
            if node in visited:
                continue
            visited.add(node)
            warehouse_distances[node] = dist
            for neighbor, weight in graph[node]:
                heapq.heappush(queue, (dist + weight, neighbor))
    
    employee_distances = {i: 0 for i in range(1, n+1)}
    for employee in employees:
        visited = set()
        queue = [(0, employee)]
        while queue:
            dist, node = heapq.heappop(queue)
            if node in visited:
                continue
            visited.add(node)
            employee_distances[node] = dist
            for neighbor, weight in graph[node]:
                heapq.heappush(queue, (dist + weight, neighbor))

    total_distance = 0
    for client in clients:
        min_distance = float('inf')
        for warehouse in warehouses:
            distance = employee_distances[client] + warehouse_distances[warehouse]
            min_distance = min(min_distance, distance)
        total_distance += min_distance

    return total_distance

# Reading input
n, m, s, t = map(int, input().split())
warehouses = list(map(int, input().split()))
employees = list(map(int, input().split()))
clients = list(map(int, input().split()))
roads = [list(map(int, input().split())) for _ in range(m)]

# Call the function and print the result
print(min_total_distance(n, m, s, t, warehouses, employees, clients, roads))
