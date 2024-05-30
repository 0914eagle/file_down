
def cheapest_fee(N, P, X, Y, partnerships, M, SWERC_banks):
    graph = {}
    for a, b, c in partnerships:
        if a not in graph:
            graph[a] = {}
        graph[a][b] = c
        if b not in graph:
            graph[b] = {}
        graph[b][a] = c
    
    SWERC_banks_set = set(SWERC_banks)
    min_fees = {bank: float('inf') for bank in range(1, N+1)}
    min_fees[X] = 0
    
    for _ in range(N):
        for node in range(1, N+1):
            if node in graph:
                for neighbor in graph[node]:
                    if min_fees[node] + graph[node][neighbor] < min_fees[neighbor]:
                        min_fees[neighbor] = min_fees[node] + graph[node][neighbor]
    
    cheapest_fee = min_fees[Y]
    
    for bank in SWERC_banks_set:
        if min_fees[bank] < cheapest_fee:
            return "Impossible"
    
    if cheapest_fee == float('inf'):
        return "Infinity"
    
    return cheapest_fee

# Input parsing
N, P, X, Y = map(int, input().split())
partnerships = [tuple(map(int, input().split())) for _ in range(P)]
M = int(input())
SWERC_banks = list(map(int, input().split())

# Compute and print the result
print(cheapest_fee(N, P, X, Y, partnerships, M, SWERC_banks))
```
