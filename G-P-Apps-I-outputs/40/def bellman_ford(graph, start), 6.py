
def bellman_ford(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if dist[node] + weight < dist[neighbor]:
                    dist[neighbor] = dist[node] + weight

    for node in graph:
        for neighbor, weight in graph[node].items():
            if dist[node] + weight < dist[neighbor]:
                return float('inf')

    return max(dist.values())

def solve_transfer_fee(N, P, X, Y, partnerships, M, swerc_banks):
    graph = {node: {} for node in range(1, N + 1)}

    for a, b, c in partnerships:
        graph[a][b] = c
        graph[b][a] = c

    swerc_nodes = set(swerc_banks)

    if X not in swerc_nodes or Y not in swerc_nodes:
        return "Impossible"

    min_fee = float('inf')
    for swerc_bank in swerc_nodes:
        graph[swerc_bank][swerc_bank] = 0
        fee = bellman_ford(graph, swerc_bank)
        min_fee = min(min_fee, fee)

    if min_fee == float('inf'):
        return "Infinity"
    else:
        return min_fee

# Read input
N, P, X, Y = map(int, input().split())
partnerships = [tuple(map(int, input().split())) for _ in range(P)]
M = int(input())
swerc_banks = list(map(int, input().split())

# Call the function and output the result
result = solve_transfer_fee(N, P, X, Y, partnerships, M, swerc_banks)
print(result)
```
