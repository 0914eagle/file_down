
import sys

def min_expected_duration(origin, destination, connections):
    graph = {}
    for connection in connections:
        source, target, departure_time, duration, delay_prob, max_delay = connection
        if source not in graph:
            graph[source] = []
        graph[source].append((target, departure_time, duration, delay_prob, max_delay))

    def get_min_expected_duration(current, current_time, total_delay):
        if current == destination:
            return total_delay

        if current not in graph:
            return sys.maxsize

        min_expected = sys.maxsize
        for connection in graph[current]:
            new_target, departure_time, duration, delay_prob, max_delay = connection
            new_time = max(departure_time, current_time + duration)

            expected_duration = total_delay * delay_prob / 100 + (1 - delay_prob / 100) * get_min_expected_duration(new_target, new_time, max(total_delay, new_time - departure_time))

            min_expected = min(min_expected, expected_duration)

        return min_expected

    ans = get_min_expected_duration(origin, 0, 0)
    return "IMPOSSIBLE" if ans == sys.maxsize else round(ans, 6)

# Input parsing
origin, destination = input().strip().split()
n = int(input())
connections = []
for _ in range(n):
    source, target, departure_time, duration, delay_prob, max_delay = input().strip().split()
    connections.append((source, target, int(departure_time), int(duration), int(delay_prob), int(max_delay))

# Call the function and print the result
result = min_expected_duration(origin, destination, connections)
print(result)
