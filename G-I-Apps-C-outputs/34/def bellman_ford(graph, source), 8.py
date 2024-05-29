
def bellman_ford(graph, source):
    dist = {node: float('inf') for node in graph}
    dist[source] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if dist[node] + weight < dist[neighbor]:
                    dist[neighbor] = dist[node] + weight

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if dist[node] + weight < dist[neighbor]:
                    return float('inf')

    return max(dist.values())


def compute_largest_fee(N, P, X, Y, partnerships, M, swerc_banks):
    graph = {i: {} for i in range(1, N+1)}

    for a, b, c in partnerships:
        graph[a][b] = c
        graph[b][a] = c

    for i in range(1, N+1):
        if i not in swerc_banks:
            graph[X][i] = 0
            graph[i][Y] = 0

    return bellman_ford(graph, X)


# Input parsing
N, P, X, Y = map(int, input().split())
partnerships = [tuple(map(int, input().split())) for _ in range(P)]
M = int(input())
swerc_banks = list(map(int, input().split())

# Compute and output result
result = compute_largest_fee(N, P, X, Y, partnerships, M, swerc_banks)
if result == float('inf'):
    print("Infinity")
else:
    print(result)
```
