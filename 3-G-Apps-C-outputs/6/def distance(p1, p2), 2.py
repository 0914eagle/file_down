
import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def find_max_towers(n, towers):
    max_towers = 0
    for i in range(n):
        for j in range(i+1, n):
            dist = distance(towers[i], towers[j])
            if dist <= 2:
                mid_x = (towers[i][0] + towers[j][0]) / 2
                mid_y = (towers[i][1] + towers[j][1]) / 2
                count = sum(1 for tower in towers if distance((mid_x, mid_y), tower) <= 1)
                max_towers = max(max_towers, count)
    return max_towers

# Read input
n = int(input())
towers = []
for _ in range(n):
    x, y = map(float, input().split())
    towers.append((x, y))

# Add one more tower at each possible location and find the maximum towers
max_towers = 0
for i in range(n):
    for j in range(i+1, n):
        new_tower_x = (towers[i][0] + towers[j][0]) / 2
        new_tower_y = (towers[i][1] + towers[j][1]) / 2
        towers.append((new_tower_x, new_tower_y))
        max_towers = max(max_towers, find_max_towers(n+1, towers))
        towers.pop()

print(max_towers)
