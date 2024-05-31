
import math

def ski_slalom(W, v_h, N, gates, S, speeds):
    min_time = float('inf')
    best_speed = -1
    
    for speed in speeds:
        current_time = 0
        x_prev = gates[0][0]
        y_prev = gates[0][1]
        
        for i in range(1, N):
            x_curr = gates[i][0]
            y_curr = gates[i][1]
            
            dist_between_gates = math.sqrt((x_curr - x_prev)**2 + (y_curr - y_prev)**2)
            
            if x_curr - x_prev > v_h * speed:
                current_time = float('inf')
                break
            
            time_to_next_gate = dist_between_gates / v_h
            if y_curr - y_prev > W:
                time_to_next_gate += (y_curr - y_prev - W) / speed
                
            current_time += time_to_next_gate
            
            x_prev = x_curr
            y_prev = y_curr
        
        if current_time < min_time:
            min_time = current_time
            best_speed = speed
    
    if best_speed == -1:
        print("IMPOSSIBLE")
    else:
        print(best_speed)

# Sample Input
W, v_h, N = 3, 2, 3
gates = [(1, 1), (5, 2), (1, 3)]
S = 3
speeds = [3, 2, 1]

ski_slalom(W, v_h, N, gates, S, speeds)
