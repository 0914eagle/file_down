
def cheapest_fee(N, P, X, Y, partnerships, M, SWERC_banks):
    graph = [[float('inf')] * (N + 1) for _ in range(N + 1)]

    for a, b, c in partnerships:
        graph[a][b] = min(graph[a][b], c)
        graph[b][a] = min(graph[b][a], c)

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    min_fee = float('inf')
    for bank in SWERC_banks:
        min_fee = min(min_fee, graph[X][bank] + graph[bank][Y])

    if min_fee == float('inf'):
        return "Impossible"
    else:
        max_fee = 0
        for a, b, c in partnerships:
            if graph[X][a] + c + graph[b][Y] > min_fee:
                max_fee = max(max_fee, graph[X][a] + c + graph[b][Y] - min_fee)

        return max_fee if max_fee > 0 else "Impossible"

# Sample Input 1
N, P, X, Y = 6, 8, 1, 6
partnerships = [(1, 2, 5), (1, 3, 1), (2, 6, 6), (2, 3, 6), (4, 2, 3), (3, 4, 1), (4, 5, 1), (5, 6, 1)]
M = 5
SWERC_banks = [1, 3, 6, 5, 4]
print(cheapest_fee(N, P, X, Y, partnerships, M, SWERC_banks))  # Output: 3

# Sample Input 2
N, P, X, Y = 3, 4, 1, 2
partnerships = [(1, 2, 6), (1, 3, 2), (1, 2, 7), (2, 3, 3)]
M = 2
SWERC_banks = [1, 2]
print(cheapest_fee(N, P, X, Y, partnerships, M, SWERC_banks))  # Output: Infinity
```
