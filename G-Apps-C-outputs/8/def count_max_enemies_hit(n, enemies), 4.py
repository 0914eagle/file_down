
import math

def count_max_enemies_hit(n, enemies):
    angles = []
    
    for x, y, r in enemies:
        d = math.sqrt(x**2 + y**2)
        if d <= r:
            angles.append((0, 0))
        else:
            angle1 = math.acos(r/d)
            angle2 = math.atan2(y, x)
            angles.append((angle2 - angle1, 1))
            angles.append((angle2 + angle1, -1))
    
    angles.sort()
    
    max_enemies = 0
    current_enemies = 0
    
    for _, change in angles:
        current_enemies += change
        max_enemies = max(max_enemies, current_enemies)
    
    return max_enemies

# Input parsing
n = int(input())
enemies = []
for _ in range(n):
    x, y, r = map(float, input().split())
    enemies.append((x, y, r))

# Call the function and output the result
print(count_max_enemies_hit(n, enemies))
