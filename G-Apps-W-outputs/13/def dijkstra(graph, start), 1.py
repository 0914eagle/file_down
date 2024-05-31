
import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

def count_edges_not_in_shortest_path(N, edges):
    graph = {i: {} for i in range(1, N+1)}
    
    for a, b, c in edges:
        graph[a][b] = c
        graph[b][a] = c
    
    all_shortest_paths = []
    for i in range(1, N+1):
        all_shortest_paths.append(dijkstra(graph, i))
    
    not_in_any_shortest_path = 0
    for edge in edges:
        a, b, c = edge
        in_shortest_path = False
        for shortest_path in all_shortest_paths:
            if shortest_path[a][b] == c:
                in_shortest_path = True
                break
        if not in_shortest_path:
            not_in_any_shortest_path += 1
    
    return not_in_any_shortest_path

# Input processing
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

# Output
print(count_edges_not_in_shortest_path(N, edges))
