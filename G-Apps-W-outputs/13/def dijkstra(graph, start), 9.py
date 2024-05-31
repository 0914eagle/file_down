
import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def count_non_shortest_edges(N, edges):
    graph = {i: {} for i in range(1, N+1)}
    for a, b, c in edges:
        graph[a][b] = c
        graph[b][a] = c

    non_shortest_edges = 0
    for i in range(len(edges)):
        a, b, c = edges[i]
        del graph[a][b]
        del graph[b][a]

        shortest_paths = {}
        for vertex in range(1, N+1):
            shortest_paths[vertex] = dijkstra(graph, vertex)

        for start in range(1, N+1):
            for end in range(start+1, N+1):
                shortest_path = shortest_paths[start][end]
                if end in shortest_path and start in shortest_path and shortest_path[end] != float('infinity'):
                    continue
                elif (start, end, c) in edges or (end, start, c) in edges:
                    non_shortest_edges += 1

        graph[a][b] = c
        graph[b][a] = c

    return non_shortest_edges

# Read input
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

# Output the result
print(count_non_shortest_edges(N, edges))
