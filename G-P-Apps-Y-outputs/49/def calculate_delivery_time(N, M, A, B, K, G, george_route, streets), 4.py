
def calculate_delivery_time(N, M, A, B, K, G, george_route, streets):
    time_blocked = set()
    for i in range(len(george_route) - 1):
        street_start = min(george_route[i], george_route[i+1])
        street_end = max(george_route[i], george_route[i+1])
        for j in range(street_start, street_end):
            for t in range(j, j + streets[(street_start, street_end)]):
                time_blocked.add(t)
    
    min_time = float('inf')
    for t in range(K, max(time_blocked) + 1):
        if t not in time_blocked:
            time_to_destination = abs(t - K) + streets[(A, B)]
            min_time = min(min_time, time_to_destination)
    
    return min_time

N, M = map(int, input().split())
A, B, K, G = map(int, input().split())
george_route = list(map(int, input().split()))
streets = {}
for _ in range(M):
    A, B, L = map(int, input().split())
    streets[(A, B)] = L

result = calculate_delivery_time(N, M, A, B, K, G, george_route, streets)
print(result)
```
