
from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(graph, start, end):
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        cur_dist, cur_node = heappop(queue)
        if cur_node == end:
            return distances[cur_node]
        for neighbor, dist in graph[cur_node]:
            if distances[neighbor] > cur_dist + dist:
                distances[neighbor] = cur_dist + dist
                heappush(queue, (distances[neighbor], neighbor))
    return distances[end]


def main():
    n, m, s, t = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        a, b, l = map(int, input().split())
        graph[a].append((b, l))
    shortest_path = dijkstra(graph, s, t)
    for a, b, l in graph.values():
        if dijkstra(graph, s, a) + l + dijkstra(graph, b, t) == shortest_path:
            print('YES')
        elif dijkstra(graph, s, a) + 1 + dijkstra(graph, b, t) == shortest_path:
            print('CAN', l - 1)
        else:
            print('NO')


if __name__ == '__main__':
    main()

