
import heapq

def min_total_distance(n, m, s, t, warehouses, employees, clients, roads):
    graph = [[] for _ in range(n+1)]
    for u, v, d in roads:
        graph[u].append((v, d))
        graph[v].append((u, d))
    
    warehouse1, warehouse2 = warehouses
    min_distances = []
    
    for client in clients:
        heap = [(0, warehouse1)]
        visited = set()
        
        while heap:
            distance, node = heapq.heappop(heap)
            if node == client:
                min_distances.append(distance)
                break
            
            if node in visited:
                continue
            
            visited.add(node)
            for neighbor, dist in graph[node]:
                heapq.heappush(heap, (distance + dist, neighbor))
        
        heap = [(0, warehouse2)]
        visited = set()
        
        while heap:
            distance, node = heapq.heappop(heap)
            if node == client:
                min_distances.append(distance)
                break
            
            if node in visited:
                continue
            
            visited.add(node)
            for neighbor, dist in graph[node]:
                heapq.heappush(heap, (distance + dist, neighbor))
    
    min_distances.sort()
    return sum(min_distances[:s])

# Parse input
n, m, s, t = map(int, input().split())
warehouses = list(map(int, input().split()))
employees = list(map(int, input().split()))
clients = list(map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]

# Call function and output result
print(min_total_distance(n, m, s, t, warehouses, employees, clients, roads))
