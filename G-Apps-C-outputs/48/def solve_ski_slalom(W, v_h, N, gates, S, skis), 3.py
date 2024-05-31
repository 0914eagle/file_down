
import math

def solve_ski_slalom(W, v_h, N, gates, S, skis):
    def time_to_pass_gate(x1, y1, x2, y2, v, v_h):
        dx = abs(x2 - x1)
        dy = y2 - y1
        return math.sqrt(dx*dx + dy*dy) / v + dx / v_h
    
    min_time = float('inf')
    best_ski = -1
    
    for ski in skis:
        current_time = 0
        current_pos = gates[0][0]
        current_v = ski
        
        for i in range(1, N):
            next_pos = gates[i][0]
            next_gate_y = gates[i][1]
            
            time_to_next_gate = time_to_pass_gate(current_pos, gates[i-1][1], next_pos, next_gate_y, current_v, v_h)
            
            if time_to_next_gate > min_time:
                break
            
            current_time += time_to_next_gate
            current_pos = next_pos
        
        if current_time < min_time:
            min_time = current_time
            best_ski = ski
    
    if best_ski == -1:
        print("IMPOSSIBLE")
    else:
        print(best_ski)

# Input parsing
W, v_h, N = map(int, input().split())
gates = [tuple(map(int, input().split())) for _ in range(N)]
S = int(input())
skis = [int(input()) for _ in range(S)]

# Call the function to solve the ski slalom problem
solve_ski_slalom(W, v_h, N, gates, S, skis)
