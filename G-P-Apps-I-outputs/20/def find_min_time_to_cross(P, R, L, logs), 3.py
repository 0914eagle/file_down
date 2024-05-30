
def find_min_time_to_cross(P, R, L, logs):
    def dfs(node, visited):
        visited.add(node)
        if node == -1:
            return 0
        min_time = float('inf')
        for log in logs:
            if node in log and len(visited.intersection(log)) == 1:
                next_node = log[1] if log[0] == node else log[0]
                time = dfs(next_node, visited.copy()) + 1
                min_time = min(min_time, time)
        return min_time

    min_time = float('inf')
    for log in logs:
        if -2 in log:
            time = dfs(-2, set()) + 1
            min_time = min(min_time, time)

    if min_time == float('inf'):
        return P
    return min_time * P

# Parse input
P, R, L = map(int, input().split())
logs = [tuple(map(int, input().split())) for _ in range(L)]

# Find the minimum time to cross
result = find_min_time_to_cross(P, R, L, logs)
print(result)
```
