
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

def count_edges_not_in_shortest_paths(N, M, edges):
    graph = {i: {} for i in range(1, N+1)}

    for a, b, c in edges:
        graph[a][b] = c
        graph[b][a] = c

    not_in_shortest_paths = 0

    for i in range(M):
        a, b, c = edges[i]
        shortest_paths_from_a = dijkstra(graph, a)
        
        if shortest_paths_from_a[b] < c:
            not_in_shortest_paths += 1

    return not_in_shortest_paths

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

result = count_edges_not_in_shortest_paths(N, M, edges)
print(result)
