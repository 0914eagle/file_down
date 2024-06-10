
from collections import deque


def find_producer(node, graph):
    producer_id = None
    for p_id, producers in enumerate(graph):
        if producers[node] == 1:
            if producer_id is None:
                producer_id = p_id
            else:
                producer_id = -1
                break
    return producer_id


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in range(len(graph)):
        if graph[start][node] == 1:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def find_max_producers(graph, producers, warehouse):
    paths = {}
    for i in range(producers):
        paths[i] = find_all_paths(graph, i, warehouse)
    max_producers = 0
    for path in paths.values():
        for p in path:
            producer_id = find_producer(p[1], graph)
            if producer_id >= 0:
                max_producers = max(max_producers, producer_id + 1)

    return max_producers


def solve(N, K, M, edges):
    graph = [[0] * N for _ in range(N)]
    for edge in edges:
        graph[edge[0] - 1][edge[1] - 1] = 1

    warehouse = N - 1
    max_producers = find_max_producers(graph, K, warehouse)
    return max_producers


N, K, M = map(int, input().split())
edges = []
for _ in range(M):
    u, v = map(int, input().split())
    edges.append((u, v))
print(solve(N, K, M, edges))

