
def min_crossing_time(P, R, L, logs):
    graph = {}
    for i in range(-2, R):
        graph[i] = []

    for log in logs:
        graph[log[0]].append(log[1])
        graph[log[1]].append(log[0])

    visited = set()
    time = 0

    def dfs(node):
        nonlocal time
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                time += 1
                dfs(neighbor)

    dfs(-2)

    if len(visited) == R + 1:  # All boulders and right bank are reachable
        return P + time
    else:
        return P - (R + 1 - len(visited))

# Input parsing
input_data = input().split()
P, R, L = map(int, input_data[:3])
logs = []
for i in range(L):
    log_input = input().split()
    logs.append((int(log_input[0]), int(log_input[1])))

# Call the function with input values
result = min_crossing_time(P, R, L, logs)
print(result)
```
