
import heapq

def min_expected_duration(origin, destination, n, connections):
    graph = {}
    for connection in connections:
        start, end, departure, duration, probability, max_delay = connection
        if start not in graph:
            graph[start] = []
        graph[start].append((end, departure, duration, probability, max_delay))

    pq = [(0, origin, 0)]  # (time, node, probability of delay)
    visited = set()

    while pq:
        time, current, prob_delay = heapq.heappop(pq)

        if current == destination:
            return round(time, 6)

        if current in visited:
            continue
        visited.add(current)

        if current in graph:
            for neighbor, departure, duration, prob, max_delay in graph[current]:
                new_prob_delay = prob_delay + prob/100
                new_time = time + departure + (1 - new_prob_delay) * duration + new_prob_delay * (duration + max_delay/2)
                heapq.heappush(pq, (new_time, neighbor, new_prob_delay))

    return "IMPOSSIBLE"

# Input parsing
origin, destination = input().strip().split()
n = int(input().strip())
connections = []
for _ in range(n):
    start, end, departure, duration, probability, max_delay = input().strip().split()
    connections.append((start, end, int(departure), int(duration), int(probability), int(max_delay))

# Call the function and print the result
result = min_expected_duration(origin, destination, n, connections)
print(result)
