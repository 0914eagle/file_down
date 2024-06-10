
import sys
from collections import defaultdict

def dijkstra(graph, start):
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    visited = set()
    while len(visited) < len(graph):
        min_dist = float('inf')
        min_node = None
        for node in graph:
            if node not in visited and dist[node] < min_dist:
                min_dist = dist[node]
                min_node = node
        visited.add(min_node)
        for neighbor in graph[min_node]:
            if neighbor not in visited:
                dist[neighbor] = min(dist[neighbor], dist[min_node] + graph[min_node][neighbor])
    return dist


def main():
    n, m, s, t = map(int, sys.stdin.readline().split())
    graph = defaultdict(dict)
    for _ in range(m):
        a, b, l = map(int, sys.stdin.readline().split())
        graph[a][b] = l
    dist = dijkstra(graph, s)
    for _ in range(m):
        a, b, l = map(int, sys.stdin.readline().split())
        if dist[b] == dist[a] + l:
            print('YES')
        elif dist[b] > dist[a] + l:
            print('CAN', l - (dist[b] - dist[a]))
        else:
            print('NO')


if __name__ == '__main__':
    main()

