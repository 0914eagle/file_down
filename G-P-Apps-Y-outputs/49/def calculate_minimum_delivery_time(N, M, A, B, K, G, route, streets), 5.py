
def calculate_minimum_delivery_time(N, M, A, B, K, G, route, streets):
    intersection_times = [0] * (N + 1)
    for i in range(1, len(route)):
        start_time = i * 5
        end_time = start_time + 5
        for j in range(start_time, end_time):
            intersection_times[route[i]] = j
    
    dist = [[float('inf')] * (N + 1) for _ in range(N + 1)]
    for a, b, l in streets:
        dist[a][b] = l
        dist[b][a] = l
    
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    min_time = float('inf')
    for i in range(1, N + 1):
        time = max(intersection_times[i] - K, dist[A][i] + dist[i][B])
        min_time = min(min_time, time)
    
    return min_time

# Input processing
N, M = map(int, input().split())
A, B, K, G = map(int, input().split())
route = list(map(int, input().split()))
streets = [list(map(int, input().split())) for _ in range(M)]

# Calculate and output the minimum delivery time
print(calculate_minimum_delivery_time(N, M, A, B, K, G, route, streets))
```
