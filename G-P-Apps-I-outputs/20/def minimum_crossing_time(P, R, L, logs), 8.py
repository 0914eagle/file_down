
def minimum_crossing_time(P, R, L, logs):
    adj = {i: [] for i in range(-2, R)}
    for log in logs:
        adj[log[0]].append(log[1])
        adj[log[1]].append(log[0])

    def dfs(node, visited):
        visited.add(node)
        for neighbor in adj[node]:
            if neighbor not in visited:
                dfs(neighbor, visited)

    visited = set()
    dfs(-2, visited)

    if -1 not in visited:
        return P

    collapse_time = 0
    while -1 not in visited:
        next_visited = visited.copy()
        for node in visited:
            for neighbor in adj[node]:
                next_visited.add(neighbor)
        visited = next_visited
        collapse_time += 1

    return P * collapse_time

# Input parsing
input_values = input().split()
P, R, L = map(int, input_values[:3])
logs = [tuple(map(int, input().split())) for _ in range(L)]

# Call the function and print the output
print(minimum_crossing_time(P, R, L, logs))
```
