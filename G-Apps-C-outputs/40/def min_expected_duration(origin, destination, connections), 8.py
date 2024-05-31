
import heapq

def min_expected_duration(origin, destination, connections):
    graph = {}
    for conn in connections:
        dep_station, arr_station, dep_time, journey_time, delay_prob, max_delay = conn
        if dep_station not in graph:
            graph[dep_station] = []
        graph[dep_station].append((arr_station, dep_time, journey_time, delay_prob, max_delay))

    pq = [(0, origin, 0)]  # (expected duration, current station, current time)
    visited = set()

    while pq:
        exp_duration, current_station, current_time = heapq.heappop(pq)

        if current_station == destination:
            return exp_duration

        if current_station in visited:
            continue

        visited.add(current_station)

        if current_station not in graph:
            continue

        for next_station, dep_time, journey_time, delay_prob, max_delay in graph[current_station]:
            for delay in range(1, max_delay + 1):
                new_time = current_time + delay
                new_exp_duration = exp_duration + journey_time + delay * delay_prob / 100
                heapq.heappush(pq, (new_exp_duration, next_station, dep_time + journey_time + delay))

    return "IMPOSSIBLE"

# Input processing
input_origin, input_destination = input().strip().split()
n = int(input())
connections = []
for _ in range(n):
    conn = input().strip().split()
    connections.append((conn[0], conn[1], int(conn[2]), int(conn[3]), int(conn[4]), int(conn[5]))

# Call the function and output the result
result = min_expected_duration(input_origin, input_destination, connections)
print(result)
