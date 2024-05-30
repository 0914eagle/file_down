
def minimum_crossing_time(P, R, L, logs):
    def dfs(node, visited, logs):
        visited.add(node)
        for log in logs:
            if node in log and log not in visited:
                next_node = log[0] if log[1] == node else log[1]
                dfs(next_node, visited, logs)
    
    reachable = set()
    dfs(-2, reachable, logs)
    
    if -1 not in reachable:
        return P
    
    total_time = 0
    for _ in range(P):
        total_time += 1
        new_reachable = set()
        for node in reachable:
            for log in logs:
                if node in log:
                    next_node = log[0] if log[1] == node else log[1]
                    new_reachable.add(next_node)
        reachable = new_reachable
        if -1 in reachable:
            break
    
    return total_time

# Input parsing
input_str = input().strip().split()
P, R, L = int(input_str[0]), int(input_str[1]), int(input_str[2])
logs = []
for _ in range(L):
    log = tuple(map(int, input().strip().split()))
    logs.append(log)

# Call the function with the input values
result = minimum_crossing_time(P, R, L, logs)
print(result)
```
