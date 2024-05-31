
import math

def min_expected_duration(origin, destination, connections):
    def get_connection_probability(connection, current_time):
        m, t, p, d = connection
        if current_time < m:
            return 0
        else:
            delay_prob = p / 100
            delay_time = math.ceil((d + 1) / 2)
            return delay_prob * delay_time
    
    def get_expected_duration(connection, current_time):
        m, t, _, _ = connection
        return max(m, current_time) + t + get_connection_probability(connection, current_time)
    
    def find_min_expected_duration(curr_loc, curr_time):
        if curr_loc == destination:
            return curr_time
        
        min_expected = float('inf')
        for connection in connections:
            origin_conn, dest_conn, _, _ = connection
            if curr_loc == origin_conn:
                expected_duration = get_expected_duration(connection, curr_time)
                next_loc = dest_conn
                next_time = expected_duration
                min_expected = min(min_expected, find_min_expected_duration(next_loc, next_time))
        
        return min_expected
    
    return find_min_expected_duration(origin, 0)

# Input parsing
origin, destination = input().strip().split()
n = int(input().strip())
connections = []
for _ in range(n):
    origin_conn, dest_conn, m, t, p, d = input().strip().split()
    connections.append((origin_conn, dest_conn, int(m), int(t), int(p), int(d))

# Call the function and print the result
result = min_expected_duration(origin, destination, connections)
if result == float('inf'):
    print("IMPOSSIBLE")
else:
    print("{:.6f}".format(result))
