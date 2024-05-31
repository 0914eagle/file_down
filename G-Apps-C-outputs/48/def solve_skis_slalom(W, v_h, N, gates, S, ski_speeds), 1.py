
import sys

def solve_skis_slalom(W, v_h, N, gates, S, ski_speeds):
    def time_to_pass_gate(x1, y1, x2, y2, v_speed, h_speed):
        delta_y = y2 - y1
        delta_x = x2 - x1
        time_v = delta_y / v_speed  # Time taken to pass gate vertically
        time_h = delta_x / h_speed  # Time taken to pass gate horizontally
        return max(time_v, time_h)

    def can_pass_course(ski_speed):
        current_x = gates[0][0]
        current_y = gates[0][1]
        for i in range(1, N):
            next_x = gates[i][0]
            next_y = gates[i][1]
            time_taken = time_to_pass_gate(current_x, current_y, next_x, next_y, ski_speed, v_h)
            if time_taken > W / ski_speed:  # Check if time taken is greater than allowed time to reach next gate
                return False
            current_x = next_x
            current_y = next_y
        return True

    min_time = sys.maxsize
    best_ski_speed = None
    for ski_speed in ski_speeds:
        if can_pass_course(ski_speed):
            time_to_finish = gates[-1][1] / ski_speed
            if time_to_finish < min_time:
                min_time = time_to_finish
                best_ski_speed = ski_speed

    if best_ski_speed is None:
        print("IMPOSSIBLE")
    else:
        print(best_ski_speed)

# Read input
W, v_h, N = map(int, input().strip().split())
gates = [list(map(int, input().strip().split())) for _ in range(N)]
S = int(input().strip())
ski_speeds = [int(input().strip()) for _ in range(S)]

# Solve the problem
solve_skis_slalom(W, v_h, N, gates, S, ski_speeds)
