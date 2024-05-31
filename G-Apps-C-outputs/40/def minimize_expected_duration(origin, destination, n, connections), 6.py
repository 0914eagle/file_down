
import sys

def minimize_expected_duration(origin, destination, n, connections):
    graph = {}
    for conn in connections:
        start, end, departure, duration, prob_delay, max_delay = conn
        if start not in graph:
            graph[start] = []
        graph[start].append((end, departure, duration, prob_delay, max_delay))

    def dfs(node, time):
        if node == destination:
            return 0.0
        if node not in graph:
            return sys.maxsize

        min_duration = sys.maxsize
        for neighbor, departure, duration, prob_delay, max_delay in graph[node]:
            expected_delay = 0.0
            for delay in range(1, max_delay+1):
                expected_delay += min(delay, max_delay) * (prob_delay / 100)
                new_time = max(departure, time) + duration + delay
                min_duration = min(min_duration, new_time + dfs(neighbor, new_time))
            min_duration += expected_delay

        return min_duration

    result = dfs(origin, 0)
    return "IMPOSSIBLE" if result == sys.maxsize else round(result, 6)

# Input processing
origin, destination = input().split()
n = int(input())
connections = []
for _ in range(n):
    conn = input().split()
    connections.append((conn[0], conn[1], int(conn[2]), int(conn[3]), int(conn[4]), int(conn[5]))

# Call the function and output the result
print(minimize_expected_duration(origin, destination, n, connections))
