
import math

W, v_h, N = map(int, input().split())
gate_positions = [list(map(int, input().split())) for _ in range(N)]
S = int(input())
ski_speeds = [int(input()) for _ in range(S)]

def time_to_reach_gate(ski_speed, gate_pos):
    h_dist = gate_pos[0]
    v_dist = gate_pos[1]
    return math.sqrt(h_dist**2 + v_dist**2) / ski_speed

def can_pass_course(ski_speed):
    current_time = 0
    last_gate_pos = gate_positions[0]
    for i in range(1, N):
        gate_pos = gate_positions[i]
        time_to_reach = time_to_reach_gate(ski_speed, gate_pos)
        time_diff = time_to_reach - current_time
        max_h_distance = time_diff * v_h
        if abs(gate_pos[0] - last_gate_pos[0]) <= max_h_distance:
            current_time = time_to_reach
            last_gate_pos = gate_pos
        else:
            return False
    return True

best_ski_speed = None
best_time = float('inf')

for ski_speed in ski_speeds:
    if can_pass_course(ski_speed):
        last_gate_pos = gate_positions[-1]
        total_time = last_gate_pos[1] / ski_speed
        if total_time < best_time:
            best_time = total_time
            best_ski_speed = ski_speed

if best_ski_speed is not None:
    print(best_ski_speed)
else:
    print("IMPOSSIBLE")
