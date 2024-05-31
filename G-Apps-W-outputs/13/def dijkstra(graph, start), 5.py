
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

def count_unreachable_edges(N, M, edges):
    graph = {i: {} for i in range(1, N+1)}
    
    for a, b, c in edges:
        graph[a][b] = c
        graph[b][a] = c
    
    unreachable_edges = 0
    
    for i in range(1, N+1):
        distances = dijkstra(graph, i)
        
        for j in range(i+1, N+1):
            if j in distances:
                for neighbor in graph[j]:
                    if neighbor != i and distances[j] == distances[neighbor] + graph[j][neighbor]:
                        unreachable_edges += 1
    
    return unreachable_edges

# Input processing
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

result = count_unreachable_edges(N, M, edges)
print(result)
