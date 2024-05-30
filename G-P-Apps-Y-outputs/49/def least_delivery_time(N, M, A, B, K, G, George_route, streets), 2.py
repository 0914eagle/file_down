
def least_delivery_time(N, M, A, B, K, G, George_route, streets):
    # Initialize an adjacency list to store the streets between intersections
    adjacency_list = {i: [] for i in range(1, N + 1)}
    
    # Populate the adjacency list with streets
    for a, b, l in streets:
        adjacency_list[a].append((b, l))
        adjacency_list[b].append((a, l))
    
    # Calculate the time intervals when the streets are blocked
    blocked_intervals = set()
    for i in range(len(George_route) - 1):
        street_start = George_route[i]
        street_end = George_route[i + 1]
        blocked_intervals.add((i, i+1, street_start, street_end))
        blocked_intervals.add((i+1, i, street_end, street_start))
    
    # Calculate the least amount of time Luka needs to make his delivery
    INF = float('inf')
    dp = {(i, j): INF for i in range(N+1) for j in range(2001)}
    dp[A, 0] = 0
    
    for t in range(2001):
        for node in range(1, N+1):
            for neighbor, cost in adjacency_list[node]:
                if (t, t+1, node, neighbor) in blocked_intervals:
                    continue
                dp[neighbor, t+cost] = min(dp[neighbor, t+cost], dp[node, t] + cost)
    
    result = min(dp[B, K+k] for k in range(2001))
    
    return result

# Read the input
N, M = map(int, input().split())
A, B, K, G = map(int, input().split())
George_route = list(map(int, input().split()))
streets = [list(map(int, input().split())) for _ in range(M)]

# Call the function and output the result
print(least_delivery_time(N, M, A, B, K, G, George_route, streets))
```
