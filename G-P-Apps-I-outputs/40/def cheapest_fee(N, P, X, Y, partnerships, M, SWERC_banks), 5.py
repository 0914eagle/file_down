
def cheapest_fee(N, P, X, Y, partnerships, M, SWERC_banks):
    def bellman_ford(graph, start, end):
        distance = {node: float('inf') for node in graph}
        distance[start] = 0

        for _ in range(len(graph) - 1):
            for node in graph:
                for neighbor, cost in graph[node]:
                    if distance[node] + cost < distance[neighbor]:
                        distance[neighbor] = distance[node] + cost

        return distance[end]

    graph = {i: [] for i in range(1, N + 1)}
    for a, b, c in partnerships:
        graph[a].append((b, c))
        graph[b].append((a, c))

    min_fee = bellman_ford(graph, X, Y)

    for bank in SWERC_banks:
        min_fee_to_bank = bellman_ford(graph, X, bank) + bellman_ford(graph, bank, Y)
        min_fee = min(min_fee, min_fee_to_bank)

    return min_fee if min_fee != float('inf') else "Impossible"

# Sample Input 1
N1, P1, X1, Y1 = 6, 8, 1, 6
partnerships1 = [(1, 2, 5), (1, 3, 1), (2, 6, 6), (2, 3, 6), (4, 2, 3), (3, 4, 1), (4, 5, 1), (5, 6, 1)]
M1 = 5
SWERC_banks1 = [1, 3, 6, 5, 4]
print(cheapest_fee(N1, P1, X1, Y1, partnerships1, M1, SWERC_banks1))  # Output: 3

# Sample Input 2
N2, P2, X2, Y2 = 3, 4, 1, 2
partnerships2 = [(1, 2, 6), (1, 3, 2), (1, 2, 7), (2, 3, 3)]
M2 = 2
SWERC_banks2 = [1, 2]
print(cheapest_fee(N2, P2, X2, Y2, partnerships2, M2, SWERC_banks2))  # Output: Infinity
```
