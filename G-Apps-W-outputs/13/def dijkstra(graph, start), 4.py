
import heapq

def dijkstra(graph, start):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distances[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distances

def count_edges_not_in_shortest_paths(N, M, edges):
    graph = [[] for _ in range(N)]
    for a, b, c in edges:
        graph[a-1].append((b-1, c))
        graph[b-1].append((a-1, c))
    
    all_shortest_paths = []
    for i in range(N):
        all_shortest_paths.append(dijkstra(graph, i))
    
    not_in_shortest_paths = 0
    for edge in edges:
        a, b, _ = edge
        is_edge_in_shortest_path = False
        for i in range(N):
            for j in range(N):
                if i != j and all_shortest_paths[i][j] == all_shortest_paths[i][a-1] + edge[2] + all_shortest_paths[b-1][j]:
                    is_edge_in_shortest_path = True
                    break
        if not is_edge_in_shortest_path:
            not_in_shortest_paths += 1
    
    return not_in_shortest_paths

# Input processing
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

print(count_edges_not_in_shortest_paths(N, M, edges))
