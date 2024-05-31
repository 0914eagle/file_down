
import math

W, v_h, N = map(int, input().split())
gates = []
for _ in range(N):
    x, y = map(int, input().split())
    gates.append((x, y))

S = int(input())
skis = []
for _ in range(S):
    skis.append(int(input()))

min_time = float('inf')
selected_ski = None

for ski_speed in skis:
    time = 0
    for i in range(1, N):
        x1, y1 = gates[i-1]
        x2, y2 = gates[i]
        dist_to_next_gate = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        time += dist_to_next_gate / min(ski_speed, v_h)

    if time < min_time:
        min_time = time
        selected_ski = ski_speed

if selected_ski:
    print(selected_ski)
else:
    print("IMPOSSIBLE")
