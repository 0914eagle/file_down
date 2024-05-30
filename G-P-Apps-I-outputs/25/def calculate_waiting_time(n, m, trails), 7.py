
def calculate_waiting_time(n, m, trails):
    adj_list = [[] for _ in range(n)]
    for u, v, d in trails:
        adj_list[u].append((v, d))
        adj_list[v].append((u, d))

    max_time = 12
    visited = [False] * n
    waiting_time = [-1] * n
    queue = [(0, 0)]  # (current cabin, time taken so far)

    while queue:
        current_cabin, time_so_far = queue.pop(0)
        visited[current_cabin] = True
        waiting_time[current_cabin] = time_so_far

        if current_cabin == n - 1:
            return waiting_time[current_cabin]

        for neighbor, time in adj_list[current_cabin]:
            if not visited[neighbor] and time_so_far + time <= max_time:
                queue.append((neighbor, time_so_far + time))

    return -1

# Input parsing
n, m = map(int, input().split())
trails = [list(map(int, input().split())) for _ in range(m)]

result = calculate_waiting_time(n, m, trails)
print(result)
```
