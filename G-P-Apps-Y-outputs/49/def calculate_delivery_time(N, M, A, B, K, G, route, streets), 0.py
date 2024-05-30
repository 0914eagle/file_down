
import heapq

def calculate_delivery_time(N, M, A, B, K, G, route, streets):
    graph = {i: [] for i in range(1, N+1)}
    for i in range(M):
        A, B, L = streets[i]
        graph[A].append((B, L))
        graph[B].append((A, L))

    george_route = route
    intersection_times = [-1] * (N+1)
    for i in range(1, len(george_route)):
        intersection_times[george_route[i]] = 10 * (i-1)

    start_time = 10 * (G-1) + K

    pq = [(start_time, A)]
    visited = set()
    while pq:
        time, node = heapq.heappop(pq)
        if node == B:
            return time
        if node in visited:
            continue
        visited.add(node)
        for neighbor, travel_time in graph[node]:
            next_time = time + travel_time
            if intersection_times[neighbor] != -1 and (next_time % 10 == intersection_times[neighbor] % 10):
                next_time += 10 - (next_time % 10)
            heapq.heappush(pq, (next_time, neighbor))

    return -1

# Input processing
N, M = map(int, input().split())
A, B, K, G = map(int, input().split())
route = list(map(int, input().split()))
streets = [list(map(int, input().split())) for _ in range(M)]

# Output calculation
result = calculate_delivery_time(N, M, A, B, K, G, route, streets)
print(result)
```
