
def min_crossing_time(P, R, L, logs):
    def bfs(graph, start, end):
        visited = set()
        queue = [(start, 0)]
        while queue:
            curr, time = queue.pop(0)
            if curr == end:
                return time
            visited.add(curr)
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    queue.append((neighbor, time + 1))
        return float('inf')

    boulder_graph = {i: [] for i in range(-2, R)}
    for log in logs:
        boulder_graph[log[0]].append(log[1])
        boulder_graph[log[1]].append(log[0])

    min_time = 0
    for _ in range(P):
        time_to_cross = bfs(boulder_graph, -2, -1)
        if time_to_cross == float('inf'):
            return P
        min_time = max(min_time, time_to_cross)
        for log in logs:
            boulder_graph[log[0]].remove(log[1])
            boulder_graph[log[1]].remove(log[0])

    return min_time

# Input processing
input_line = input().split()
P = int(input_line[0])
R = int(input_line[1])
L = int(input_line[2])

logs = []
for _ in range(L):
    log_line = input().split()
    logs.append((int(log_line[0]), int(log_line[1])))

print(min_crossing_time(P, R, L, logs))
```
