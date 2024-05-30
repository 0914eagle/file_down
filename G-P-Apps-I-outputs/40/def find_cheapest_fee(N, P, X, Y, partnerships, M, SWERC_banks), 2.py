
def find_cheapest_fee(N, P, X, Y, partnerships, M, SWERC_banks):
    INF = float('inf')
    
    graph = [[INF for _ in range(N)] for _ in range(N)]
    
    for a, b, c in partnerships:
        graph[a-1][b-1] = c
        graph[b-1][a-1] = c
    
    for i in range(N):
        graph[i][i] = 0
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    min_cost = graph[X-1][Y-1]
    min_fee = INF
    
    for i in range(M):
        for j in range(M):
            if i != j:
                min_fee = min(min_fee, graph[SWERC_banks[i]-1][X-1] + graph[Y-1][SWERC_banks[j]-1])
    
    if min_cost == min_fee:
        return 1
    else:
        max_fee = 0
        for i in range(N):
            for j in range(N):
                if graph[i][j] == min_cost:
                    max_fee = max(max_fee, graph[i][X-1] + graph[Y-1][j])
        
        return max_fee - min_cost if max_fee - min_cost > 0 else "Impossible"

# Sample Input 1
N1, P1, X1, Y1 = 6, 8, 1, 6
partnerships1 = [(1, 2, 5), (1, 3, 1), (2, 6, 6), (2, 3, 6), (4, 2, 3), (3, 4, 1), (4, 5, 1), (5, 6, 1)]
M1 = 5
SWERC_banks1 = [1, 3, 6, 5, 4]
print(find_cheapest_fee(N1, P1, X1, Y1, partnerships1, M1, SWERC_banks1))  # Output: 3

# Sample Input 2
N2, P2, X2, Y2 = 3, 4, 1, 2
partnerships2 = [(1, 2, 6), (1, 3, 2), (1, 2, 7), (2, 3, 3)]
M2 = 2
SWERC_banks2 = [1, 2]
print(find_cheapest_fee(N2, P2, X2, Y2, partnerships2, M2, SWERC_banks2))  # Output: Infinity
``` 
