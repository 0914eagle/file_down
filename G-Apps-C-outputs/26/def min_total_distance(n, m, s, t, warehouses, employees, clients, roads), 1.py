
import heapq

def min_total_distance(n, m, s, t, warehouses, employees, clients, roads):
    graph = [[] for _ in range(n + 1)]
    for u, v, d in roads:
        graph[u].append((v, d))
        graph[v].append((u, d))
    
    warehouse1, warehouse2 = warehouses
    dist_to_clients = []
    
    for client in clients:
        heap = [(0, warehouse1)]
        visited = set()
        
        while heap:
            dist, node = heapq.heappop(heap)
            
            if node == client:
                dist_to_clients.append(dist)
                break
            
            if node in visited:
                continue
            
            visited.add(node)
            
            for neighbor, road_dist in graph[node]:
                heapq.heappush(heap, (dist + road_dist, neighbor))
        
        heap = [(0, warehouse2)]
        visited = set()
        
        while heap:
            dist, node = heapq.heappop(heap)
            
            if node == client:
                dist_to_clients.append(dist)
                break
            
            if node in visited:
                continue
            
            visited.add(node)
            
            for neighbor, road_dist in graph[node]:
                heapq.heappush(heap, (dist + road_dist, neighbor))
    
    dist_to_clients.sort()
    return sum(dist_to_clients[:s])

# Input parsing
n, m, s, t = map(int, input().split())
warehouses = list(map(int, input().split()))
employees = list(map(int, input().split()))
clients = list(map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(m)]

# Call the function with the input
result = min_total_distance(n, m, s, t, warehouses, employees, clients, roads)
print(result)
