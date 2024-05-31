
import math

def get_angle(x, y):
    return math.atan2(y, x)

def count_opponents_hit(n, opponents):
    angles = []
    for x, y, r in opponents:
        dist = math.sqrt(x**2 + y**2)
        if dist <= r:
            angles.append((0, True))
            continue
        angle = math.acos(r / dist)
        theta = get_angle(x, y)
        angles.append((theta - angle, True))
        angles.append((theta + angle, False))
    
    angles.sort(key=lambda x: (x[0], not x[1]))
    
    max_opponents_hit = 0
    current_opponents_hit = 0
    for _, is_start in angles:
        if is_start:
            current_opponents_hit += 1
        else:
            current_opponents_hit -= 1
        max_opponents_hit = max(max_opponents_hit, current_opponents_hit)
    
    return max_opponents_hit

# Input
n = int(input())
opponents = [list(map(float, input().split())) for _ in range(n)]

# Solve and output
result = count_opponents_hit(n, opponents)
print(result)
