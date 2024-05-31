
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

def solve_shortest_path_edges(N, M, edges):
    graph = {i: {} for i in range(1, N+1)}
    
    for a, b, c in edges:
        graph[a][b] = c
        graph[b][a] = c
    
    shortest_paths = {}
    
    for i in range(1, N+1):
        shortest_paths[i] = dijkstra(graph, i)
    
    no_shortest_path_edges = 0
    
    for a, b, c in edges:
        if shortest_paths[a][b] < c:
            no_shortest_path_edges += 1
    
    return no_shortest_path_edges

# Reading input
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

# Calling the function and printing the result
result = solve_shortest_path_edges(N, M, edges)
print(result)
