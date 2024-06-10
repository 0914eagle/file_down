
from collections import defaultdict
from heapq import heappush, heappop


def dijkstra(graph, start, end):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    heap = [(0, start)]
    while heap:
        distance, vertex = heappop(heap)
        if vertex == end:
            return distances[vertex]
        for neighbour, weight in graph[vertex]:
            if distances[neighbour] > distances[vertex] + weight:
                distances[neighbour] = distances[vertex] + weight
                heappush(heap, (distances[neighbour], neighbour))
    return distances[end]


def solve(n, m, s, t, roads):
    graph = defaultdict(list)
    for a, b, l in roads:
        graph[a].append((b, l))
    shortest_path = dijkstra(graph, s, t)
    for a, b, l in roads:
        if dijkstra(graph, s, a) + l + dijkstra(graph, b, t) == shortest_path:
            print('YES')
        elif dijkstra(graph, s, a) + 1 + dijkstra(graph, b, t) == shortest_path:
            print('CAN', l - 1)
        else:
            print('NO')


if __name__ == '__main__':
    n, m, s, t = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(m)]
    solve(n, m, s, t, roads)

