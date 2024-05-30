
from collections import defaultdict

def cheapest_fee(N, P, X, Y, partnerships, M, swerc_banks):
    graph = defaultdict(dict)
    for a, b, c in partnerships:
        graph[a][b] = c
        graph[b][a] = c
    
    for k in swerc_banks:
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i != j and j in graph[k] and i in graph[k]:
                    if j not in graph[i] or graph[i][j] > graph[i][k] + graph[k][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]
    
    if X not in graph or Y not in graph[X]:
        return "Impossible"
    
    if graph[X][Y] == float('inf'):
        return "Infinity"
    
    max_fee = 0
    for a in swerc_banks:
        if a in graph[X] and Y in graph[a] and max_fee < graph[X][a] + graph[a][Y]:
            max_fee = graph[X][a] + graph[a][Y]
    
    return max_fee

# Example usage
N, P, X, Y = 6, 8, 1, 6
partnerships = [(1, 2, 5), (1, 3, 1), (2, 6, 6), (2, 3, 6), (4, 2, 3), (3, 4, 1), (4, 5, 1), (5, 6, 1)]
M, swerc_banks = 5, [1, 3, 6, 5, 4]
print(cheapest_fee(N, P, X, Y, partnerships, M, swerc_banks))

N, P, X, Y = 3, 4, 1, 2
partnerships = [(1, 2, 6), (1, 3, 2), (1, 2, 7), (2, 3, 3)]
M, swerc_banks = 2, [1, 2]
print(cheapest_fee(N, P, X, Y, partnerships, M, swerc_banks))
```
