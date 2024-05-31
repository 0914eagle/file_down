
import math

def angle_between_points(x, y):
    return math.atan2(y, x)

def count_opponents_hit(n, opponents):
    angles = []
    for x, y, r in opponents:
        dist = math.sqrt(x**2 + y**2)
        if dist <= r:  # Bergur is inside opponent's circle
            angles.append((0, 0))
        else:
            angle = math.acos(r / dist)
            angle1 = angle_between_points(x, y) - angle
            angle2 = angle_between_points(x, y) + angle
            angles.append((angle1, 1))
            angles.append((angle2, -1))
    
    angles.sort(key=lambda x: (x[0], -x[1]))
    
    max_opponents_hit = 0
    current_opponents_hit = 0
    
    for angle in angles:
        current_opponents_hit += angle[1]
        max_opponents_hit = max(max_opponents_hit, current_opponents_hit)
    
    return max_opponents_hit

# Input
n = int(input())
opponents = []
for _ in range(n):
    x, y, r = map(float, input().split())
    opponents.append((x, y, r))

# Output
print(count_opponents_hit(n, opponents))
