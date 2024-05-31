
import math

def min_expected_duration(origin, destination, train_connections):
    graph = {}
    for connection in train_connections:
        start, end, dep_time, duration, prob_delay, max_delay = connection
        if start not in graph:
            graph[start] = []
        graph[start].append((end, dep_time, duration, prob_delay, max_delay))

    def get_expected_duration(node, current_time, current_delay):
        if current_time > 1200:  # Max travel time 20 hours
            return math.inf
        if node == destination:
            return current_time

        min_expected = math.inf
        if node in graph:
            for neighbor, dep_time, duration, prob_delay, max_delay in graph[node]:
                for delay in range(1, max_delay+1):
                    new_time = current_time + dep_time + delay
                    new_delay = min(current_delay + delay, max_delay)
                    prob_no_delay = 1 - prob_delay/100
                    expected_duration = get_expected_duration(neighbor, new_time, new_delay)
                    min_expected = min(min_expected, prob_delay/100 * (new_time + duration) + prob_no_delay * expected_duration)
        return min_expected

    result = get_expected_duration(origin, 0, 0)
    return result if result != math.inf else "IMPOSSIBLE"

# Sample Input 1
origin_dest = "Hamburg Bremen"
n = 3
train_connections = [
    ("Hamburg", "Bremen", 15, 68, 10, 5),
    ("Hamburg", "Bremen", 46, 55, 50, 60),
    ("Bremen", "Frankfurt", 14, 226, 10, 120)
]

print(min_expected_duration(*origin_dest.split(), train_connections))

# Sample Input 2
origin_dest2 = "Amsterdam Rotterdam"
n2 = 1
train_connections2 = [("Amsterdam", "Utrecht", 10, 22, 5, 10)]

print(min_expected_duration(*origin_dest2.split(), train_connections2))
