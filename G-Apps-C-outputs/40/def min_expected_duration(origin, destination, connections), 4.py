
import sys

def min_expected_duration(origin, destination, connections):
    def dp(curr_time, curr_station):
        if curr_station == destination:
            return 0.0
        
        if (curr_time, curr_station) in memo:
            return memo[(curr_time, curr_station)]
        
        best_duration = float('inf')
        for connection in connections:
            if connection[0] == curr_station and connection[1] != curr_station and connection[2] >= curr_time:
                delay_prob = connection[4] / 100.0
                max_delay = connection[5]
                time_delayed = max(0, min(max_delay, curr_time + connection[3] - connection[2]))
                expected_delayed_time = (1 - delay_prob) * (connection[3] + dp(curr_time + connection[3], connection[1])) + delay_prob * (connection[3] + time_delayed + dp(curr_time + connection[3] + time_delayed, connection[1]))
                best_duration = min(best_duration, expected_delayed_time)
        
        memo[(curr_time, curr_station)] = best_duration
        return best_duration

    memo = {}
    min_duration = dp(0, origin)
    
    return min_duration if min_duration != float('inf') else "IMPOSSIBLE"

# Read input
input_lines = sys.stdin.readlines()
origin, destination = input_lines[0].strip().split()
n = int(input_lines[1])

connections = []
for i in range(2, 2 + n):
    conn_info = input_lines[i].strip().split()
    connections.append((conn_info[0], conn_info[1], int(conn_info[2]), int(conn_info[3]), int(conn_info[4]), int(conn_info[5]))

# Calculate minimum expected duration
result = min_expected_duration(origin, destination, connections)
print(result)
