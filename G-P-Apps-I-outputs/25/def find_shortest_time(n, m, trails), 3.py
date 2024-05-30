
def find_shortest_time(n, m, trails):
    # Initialize a dictionary to store the minimum time to reach each cabin
    min_time = {i: float('inf') for i in range(n)}

    # Initialize the starting cabin with time 0
    min_time[0] = 0

    # Run Bellman-Ford algorithm to find the shortest time to reach each cabin
    for _ in range(n - 1):
        for u, v, d in trails:
            if min_time[u] + d < min_time[v]:
                min_time[v] = min_time[u] + d

    # Calculate the waiting time at the destination for Dr. Knight
    waiting_time = min_time[n - 1] // 12 * 12

    if min_time[n - 1] % 12 != 0:
        waiting_time += 12

    return waiting_time

# Read input
n, m = map(int, input().split())
trails = []
for _ in range(m):
    u, v, d = map(int, input().split())
    trails.append((u, v, d))

# Call the function and print the result
print(find_shortest_time(n, m, trails))
```
