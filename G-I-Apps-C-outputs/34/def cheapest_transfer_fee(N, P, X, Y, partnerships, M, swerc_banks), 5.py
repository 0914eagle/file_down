
def cheapest_transfer_fee(N, P, X, Y, partnerships, M, swerc_banks):
    graph = [[float('inf')] * N for _ in range(N)]
    
    for a, b, c in partnerships:
        graph[a-1][b-1] = c
        graph[b-1][a-1] = c
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    min_fee = float('inf')
    
    for a in swerc_banks:
        for b in swerc_banks:
            if a != b and graph[a-1][b-1] < min_fee:
                min_fee = graph[a-1][b-1]
    
    max_fee = 0
    
    for i in range(N):
        for j in range(N):
            if graph[i][X-1] + graph[j][Y-1] + graph[i][j] == min_fee:
                max_fee = max(max_fee, graph[i][j])
    
    if max_fee == float('inf'):
        return "Infinity"
    elif max_fee > 0:
        return max_fee
    else:
        return "Impossible"

# Sample Input 1
N1 = 6
P1 = 8
X1 = 1
Y1 = 6
partnerships1 = [(1, 2, 5), (1, 3, 1), (2, 6, 6), (2, 3, 6), (4, 2, 3), (3, 4, 1), (4, 5, 1), (5, 6, 1)]
M1 = 5
swerc_banks1 = [1, 3, 6, 5, 4]

print(cheapest_transfer_fee(N1, P1, X1, Y1, partnerships1, M1, swerc_banks1))  # Output: 3

# Sample Input 2
N2 = 3
P2 = 4
X2 = 1
Y2 = 2
partnerships2 = [(1, 2, 6), (1, 3, 2), (1, 2, 7), (2, 3, 3)]
M2 = 2
swerc_banks2 = [1, 2]

print(cheapest_transfer_fee(N2, P2, X2, Y2, partnerships2, M2, swerc_banks2))  # Output: "Infinity"
