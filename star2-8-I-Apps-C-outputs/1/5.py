
import sys
import networkx as nx

def solve(N, K, edges):
    graph = nx.DiGraph()
    graph.add_edges_from(edges)
    for junction in range(1, K + 1):
        if not nx.has_path(graph, junction, N):
            return 0

    for junction in range(1, N + 1):
        if not nx.has_path(graph, junction, N):
            return 0

    for i in range(1, K + 1):
        for j in range(i + 1, K + 1):
            if nx.has_path(graph, i, j):
                return 1

    return K

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N, K, M = map(int, sys.stdin.readline().strip().split())
    edges = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]
    print(solve(N, K, edges))

