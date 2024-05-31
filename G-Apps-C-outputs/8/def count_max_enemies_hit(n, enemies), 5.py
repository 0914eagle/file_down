
import math

def count_max_enemies_hit(n, enemies):
    angles = []
    
    for x, y, r in enemies:
        dist = math.sqrt(x**2 + y**2)
        
        if dist <= r:
            angle1 = math.atan2(y, x) + math.acos(dist / r)
            angle2 = math.atan2(y, x) - math.acos(dist / r)
            
            angles.append((angle1, 1))
            angles.append((angle2, -1))
        else:
            angle = math.atan2(y, x)
            angles.append((angle, 1))
            angles.append((angle + 2*math.acos(r / dist), -1))
    
    angles.sort()
    
    max_enemies = 0
    curr_enemies = 0
    
    for _, event in angles:
        curr_enemies += event
        max_enemies = max(max_enemies, curr_enemies)
    
    return max_enemies

# Input
n = int(input())
enemies = []
for _ in range(n):
    x, y, r = map(float, input().split())
    enemies.append((x, y, r))

# Output
print(count_max_enemies_hit(n, enemies))
