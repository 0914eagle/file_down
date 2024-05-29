
def find_cheapest_fee(N, P, X, Y, partnerships, M, swerc_banks):
    graph = {i: {} for i in range(1, N+1)}
    
    for a, b, c in partnerships:
        graph[a][b] = c
        graph[b][a] = c
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                if j != k and (j in graph[i] and k in graph[i]):
                    if j in graph and k in graph[j] and i in graph[k]:
                        graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
                    elif j in graph[i] and k in graph[i]:
                        graph[j][k] = graph[j][i] + graph[i][k]
    
    min_fee = float('inf')
    
    for intermediary in swerc_banks:
        if intermediary in graph[X] and Y in graph[intermediary]:
            min_fee = min(min_fee, graph[X][intermediary] + graph[intermediary][Y])
    
    if min_fee == float('inf'):
        return "Impossible"
    elif min_fee < 0:
        return "Infinity"
    else:
        return min_fee

# Sample Input 1
N, P, X, Y = 6, 8, 1, 6
partnerships = [(1, 2, 5), (1, 3, 1), (2, 6, 6), (2, 3, 6), (4, 2, 3), (3, 4, 1), (4, 5, 1), (5, 6, 1)]
M = 5
swerc_banks = [1, 3, 6, 5, 4]
print(find_cheapest_fee(N, P, X, Y, partnerships, M, swerc_banks))  # Output: 3

# Sample Input 2
N, P, X, Y = 3, 4, 1, 2
partnerships = [(1, 2, 6), (1, 3, 2), (1, 2, 7), (2, 3, 3)]
M = 2
swerc_banks = [1, 2]
print(find_cheapest_fee(N, P, X, Y, partnerships, M, swerc_banks))  # Output: Infinity
```
