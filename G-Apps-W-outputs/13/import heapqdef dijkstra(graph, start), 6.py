
import sys
from collections import defaultdict
import heapq

def dijkstra(graph, start):
    pq = [(0, start)]
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return dist

def count_edges_not_in_shortest_paths(N, edges):
    graph = defaultdict(list)
    for a, b, c in edges:
        graph[a].append((b, c))
        graph[b].append((a, c))

    result = 0
    for i in range(N):
        dist = dijkstra(graph, i+1)
        for j in range(i+1, N):
            if j+1 in dist:
                for neighbor, weight in graph[j+1]:
                    if neighbor != i+1 and dist[neighbor] == dist[j+1] + weight:
                        result += 1

    return result

if __name__ == "__main__":
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]

    print(count_edges_not_in_shortest_paths(N, edges))
