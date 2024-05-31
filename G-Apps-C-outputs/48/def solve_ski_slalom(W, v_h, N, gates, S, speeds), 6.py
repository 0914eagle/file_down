
import math

def solve_ski_slalom(W, v_h, N, gates, S, speeds):
    min_time = math.inf
    best_speed = -1
    
    for speed in speeds:
        current_time = 0
        current_x = 0
        for i in range(N):
            x, y = gates[i]
            target_x = x + (y - current_time) * v_h
            time_to_target = abs(target_x - current_x) / v_h
            current_time += time_to_target
            current_x = target_x
            gate_time = abs((y - current_time) / speed)
            current_time += gate_time
            
        if current_x <= W:
            if current_time < min_time:
                min_time = current_time
                best_speed = speed
                
    if best_speed == -1:
        print("IMPOSSIBLE")
    else:
        print(best_speed)

# Input parsing
W, v_h, N = map(int, input().split())
gates = [list(map(int, input().split())) for _ in range(N)]
S = int(input())
speeds = [int(input()) for _ in range(S)]

# Calling the function with the input values
solve_ski_slalom(W, v_h, N, gates, S, speeds)
