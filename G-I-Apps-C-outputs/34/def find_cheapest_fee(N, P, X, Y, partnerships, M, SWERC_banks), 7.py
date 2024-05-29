
def find_cheapest_fee(N, P, X, Y, partnerships, M, SWERC_banks):
    # Create a dictionary to store the partnerships and their corresponding fees
    partnership_fees = {}
    for a, b, c in partnerships:
        partnership_fees[(a, b)] = c
        partnership_fees[(b, a)] = c
    
    # Initialize a matrix to store the cheapest fees from each bank to every other bank
    INF = float('inf')
    cheapest_fees = [[INF for _ in range(N+1)] for _ in range(N+1)]
    
    # Initialize the fees for direct partnerships
    for a, b in partnership_fees:
        cheapest_fees[a][b] = partnership_fees[(a, b)]
    
    # Floyd-Warshall algorithm to find the cheapest fee between any two banks
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                cheapest_fees[i][j] = min(cheapest_fees[i][j], cheapest_fees[i][k] + cheapest_fees[k][j])
    
    max_fee = -1
    for i in SWERC_banks:
        max_fee = max(max_fee, cheapest_fees[i][X] + cheapest_fees[i][Y])
    
    if max_fee == INF:
        return "Infinity"
    else:
        return max_fee

# Input parsing
N, P, X, Y = map(int, input().split())
partnerships = [tuple(map(int, input().split())) for _ in range(P)]
M = int(input())
SWERC_banks = list(map(int, input().split())

result = find_cheapest_fee(N, P, X, Y, partnerships, M, SWERC_banks)
print(result)
```
