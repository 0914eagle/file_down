
import math

def create_adjacency_matrix(n, edges):
    adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for u, v in edges:
        adj_matrix[u][v] = 1
        adj_matrix[v][u] = 1
    return adj_matrix


def dfs(adj_matrix, visited, current):
    visited[current] = True
    for neighbour in range(len(adj_matrix)):
        if adj_matrix[current][neighbour] and not visited[neighbour]:
            dfs(adj_matrix, visited, neighbour)


def connected_components(adj_matrix):
    visited = [False] * len(adj_matrix)
    components = 0
    for node in range(len(adj_matrix)):
        if not visited[node]:
            dfs(adj_matrix, visited, node)
            components += 1
    return components


def probability_of_success(n, l, walk, edges):
    adj_matrix = create_adjacency_matrix(n, edges)
    components = connected_components(adj_matrix)
    probability = math.exp(-2 * l * components)
    return probability


n = int(input())
l = int(input())
walk = list(map(int, input().split()))
edges = []
for _ in range(n):
    edge = list(map(int, input().split()))
    edges.append(edge[1:])
probability = probability_of_success(n, l, walk, edges)
print(probability)

