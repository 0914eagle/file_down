
import sys

# Read input
W, v_h, N = map(int, input().split())
gates = []
for _ in range(N):
    x, y = map(int, input().split())
    gates.append((x, y))

S = int(input())
skis = []
for _ in range(S):
    skis_speed = int(input())
    skis.append(skis_speed)

# Initialize variables
min_time = sys.maxsize
selected_skis = -1

# Iterate through each pair of skis to find the one with the shortest time
for skis_speed in skis:
    time = 0
    current_x = 0
    current_y = 0

    for i in range(N):
        x, y = gates[i]
        gate_distance = ((x - current_x) ** 2 + (y - current_y) ** 2) ** 0.5
        
        # Calculate time taken to reach the gate
        time_to_gate = gate_distance / skis_speed
        
        # Calculate time taken to pass through the gate
        if i > 0:
            time_to_pass_gate = (y - gates[i-1][1]) / v_h
        else:
            time_to_pass_gate = 0
            
        # Update current position
        current_x = x
        current_y = y

        time += max(time_to_gate, time_to_pass_gate)

    # Calculate time to finish after passing all gates
    time += (current_y / skis_speed)
    
    if time < min_time:
        min_time = time
        selected_skis = skis_speed

# Output the result
if selected_skis == -1:
    print("IMPOSSIBLE")
else:
    print(selected_skis)
