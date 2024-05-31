
def shortest_time_skis(W, v_h, N, gates, S, skis):
    def time_to_reach_gate(x1, y1, x2, y2, v_down, v_h):
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        time = distance / v_h
        time_to_vertical_distance = abs(y2 - y1) / v_down
        return max(time, time_to_vertical_distance)
    
    min_time = float('inf')
    best_ski = None
    
    for ski_speed in skis:
        current_time = 0
        x_current = 0
        
        for i in range(N):
            x1, y1 = gates[i]
            x2, y2 = gates[i+1] if i+1 < N else (W, 0)
            
            time_to_gate = time_to_reach_gate(x_current, 0, x1, y1, ski_speed, v_h)
            current_time += time_to_gate
            x_current = x1
            
            time_to_gate = time_to_reach_gate(x_current, 0, x2, y2, ski_speed, v_h)
            current_time += time_to_gate
            x_current = x2
        
        if current_time < min_time:
            min_time = current_time
            best_ski = ski_speed
    
    if min_time == float('inf'):
        print("IMPOSSIBLE")
    else:
        print(best_ski)

# Sample Input
W, v_h, N = 3, 2, 3
gates = [(1, 1), (5, 2), (1, 3)]
S = 3
skis = [3, 2, 1]

shortest_time_skis(W, v_h, N, gates, S, skis)
