
import sys

def find_min_expected_duration(origin, destination, connections):
    graph = {}
    for conn in connections:
        dep, dest, dep_time, journey_time, prob_delay, max_delay = conn
        if dep not in graph:
            graph[dep] = []
        graph[dep].append((dest, dep_time, journey_time, prob_delay, max_delay))

    def dfs(node, time):
        if node == destination:
            return 0

        min_duration = sys.float_info.max
        for neighbor, dep_time, journey_time, prob_delay, max_delay in graph.get(node, []):
            for delay in range(1, max_delay+1):
                new_time = max(time + dep_time + delay, dep_time + journey_time)
                expected_duration = (1 - prob_delay / 100) * journey_time + prob_delay / 100 * (delay + dfs(neighbor, new_time))
                min_duration = min(min_duration, expected_duration)

        return min_duration

    result = dfs(origin, 0)
    return "IMPOSSIBLE" if result == sys.float_info.max else round(result, 6)

# Parse input
origin, destination = input().strip().split()
n = int(input().strip())
connections = []
for _ in range(n):
    dep, dest, dep_time, journey_time, prob_delay, max_delay = input().strip().split()
    connections.append((dep, dest, int(dep_time), int(journey_time), int(prob_delay), int(max_delay))

# Call the function and output the result
result = find_min_expected_duration(origin, destination, connections)
print(result)
