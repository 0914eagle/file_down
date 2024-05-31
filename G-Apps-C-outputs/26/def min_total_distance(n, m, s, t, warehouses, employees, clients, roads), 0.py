
import heapq

def min_total_distance(n, m, s, t, warehouses, employees, clients, roads):
    graph = {i: [] for i in range(1, n+1)}
    
    for u, v, d in roads:
        graph[u].append((v, d))
        graph[v].append((u, d))
    
    def dijkstra(src):
        distances = {i: float('inf') for i in range(1, n+1)}
        distances[src] = 0
        pq = [(0, src)]
        
        while pq:
            dist, node = heapq.heappop(pq)
            
            if dist > distances[node]:
                continue
            
            for neighbor, edge_dist in graph[node]:
                new_dist = dist + edge_dist
                
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
        
        return distances
    
    distances_from_warehouses = [dijkstra(warehouse) for warehouse in warehouses]
    
    min_total_distance = float('inf')
    
    for i in range(s):
        for j in range(t):
            employee = employees[i]
            client = clients[j]
            total_distance = distances_from_warehouses[0][employee] + distances_from_warehouses[1][client]
            min_total_distance = min(min_total_distance, total_distance)
    
    return min_total_distance

# Reading input
n, m, s, t = map(int, input().split())
warehouses = list(map(int, input().split()))
employees = list(map(int, input().split()))
clients = list(map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(m)]

# Calling the function and printing the result
print(min_total_distance(n, m, s, t, warehouses, employees, clients, roads))
