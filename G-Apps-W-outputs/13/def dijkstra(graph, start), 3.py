
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

N, M = map(int, input().split())
graph = {i: {} for i in range(1, N+1)}

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

shortest_paths = {}
for i in range(1, N+1):
    shortest_paths[i] = dijkstra(graph, i)

not_in_shortest_path = 0
for i in range(1, N+1):
    for j in range(i+1, N+1):
        for neighbor, weight in graph[i].items():
            if neighbor != j:
                if shortest_paths[i][j] == shortest_paths[i][neighbor] + weight:
                    break
        else:
            not_in_shortest_path += 1

print(not_in_shortest_path)
