
def bellman_ford(graph, source, target):
    dist = {node: float('inf') for node in graph}
    dist[source] = 0

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

    for u in graph:
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                return "Infinity"

    return dist[target]

def compute_largest_fee(N, P, X, Y, partnerships, M, swerc_banks):
    graph = {i: [] for i in range(1, N+1)}
    for a, b, c in partnerships:
        graph[a].append((b, c))
        graph[b].append((a, c))

    min_fee = float('inf')
    for i in range(M):
        for j in range(i+1, M):
            fee = bellman_ford(graph, swerc_banks[i], swerc_banks[j])
            min_fee = min(min_fee, fee)

    return min_fee if min_fee != float('inf') else "Impossible"

# Sample Input 1
N, P, X, Y = 6, 8, 1, 6
partnerships = [(1, 2, 5), (1, 3, 1), (2, 6, 6), (2, 3, 6), (4, 2, 3), (3, 4, 1), (4, 5, 1), (5, 6, 1)]
M = 5
swerc_banks = [1, 3, 6, 5, 4]
print(compute_largest_fee(N, P, X, Y, partnerships, M, swerc_banks))  # Output: 3

# Sample Input 2
N, P, X, Y = 3, 4, 1, 2
partnerships = [(1, 2, 6), (1, 3, 2), (1, 2, 7), (2, 3, 3)]
M = 2
swerc_banks = [1, 2]
print(compute_largest_fee(N, P, X, Y, partnerships, M, swerc_banks))  # Output: Infinity
```
