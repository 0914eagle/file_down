
def cheapest_transfer_fee(N, P, X, Y, partnerships, M, SWERC_banks):
    graph = {i: {} for i in range(1, N + 1)}
    fees = {}
    
    for a, b, c in partnerships:
        graph[a][b] = c
        graph[b][a] = c
    
    for i in range(1, N + 1):
        fees[i] = float('inf')
    
    fees[X] = 0
    visited = set()
    q = [X]
    
    while q:
        node = q.pop(0)
        visited.add(node)
        
        for neighbor, fee in graph[node].items():
            if fees[neighbor] > max(fees[node], fee):
                fees[neighbor] = max(fees[node], fee)
                q.append(neighbor)
    
    if fees[Y] == float('inf'):
        return "Impossible"
    elif fees[Y] == 0:
        return "Infinity"
    else:
        return fees[Y]

# Example usage:
N, P, X, Y = map(int, input().split())
partnerships = [tuple(map(int, input().split())) for _ in range(P)]
M = int(input())
SWERC_banks = list(map(int, input().split()))

result = cheapest_transfer_fee(N, P, X, Y, partnerships, M, SWERC_banks)
print(result)
