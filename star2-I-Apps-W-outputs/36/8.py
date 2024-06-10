
import sys
import heapq

def dijkstra(graph, start, end):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    heap = [(0, start)]
    while heap:
        current_distance, current_vertex = heapq.heappop(heap)
        if current_vertex == end:
            return distances[end]
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    return distances[end]


def main():
    n, m, s, t = map(int, sys.stdin.readline().split())
    graph = {vertex: [] for vertex in range(1, n + 1)}
    for _ in range(m):
        a, b, l = map(int, sys.stdin.readline().split())
        graph[a].append((b, l))
    min_distance = dijkstra(graph, s, t)
    for _ in range(m):
        a, b, l = map(int, sys.stdin.readline().split())
        if dijkstra(graph, s, t) > min_distance:
            print('CAN', l - 1)
        elif dijkstra(graph, s, t) == min_distance:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()

