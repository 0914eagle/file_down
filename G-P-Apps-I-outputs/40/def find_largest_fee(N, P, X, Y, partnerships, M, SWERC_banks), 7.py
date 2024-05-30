
def find_largest_fee(N, P, X, Y, partnerships, M, SWERC_banks):
    def bellman_ford(graph, start, end):
        distances = {node: float('inf') for node in graph}
        distances[start] = 0

        for _ in range(len(graph) - 1):
            for node in graph:
                for neighbor, weight in graph[node]:
                    if distances[node] + weight < distances[neighbor]:
                        distances[neighbor] = distances[node] + weight

        for node in graph:
            for neighbor, weight in graph[node]:
                if distances[node] + weight < distances[neighbor]:
                    return float('inf')

        return distances[end]

    graph = {i: [] for i in range(1, N+1)}
    for a, b, c in partnerships:
        graph[a].append((b, c))
        graph[b].append((a, c))

    cheapest_fee = bellman_ford(graph, X, Y)

    if cheapest_fee == float('inf'):
        return "Impossible"
    else:
        largest_fee = max([partner[2] for partner in partnerships])
        if cheapest_fee - largest_fee > 0:
            return largest_fee
        else:
            return "Impossible"

# Input processing
inp = list(map(int, input().split()))
N, P, X, Y = inp[:4]
partnerships = [list(map(int, input().split())) for _ in range(P)]
M = int(input())
SWERC_banks = list(map(int, input().split()))

result = find_largest_fee(N, P, X, Y, partnerships, M, SWERC_banks)
print(result)
```
