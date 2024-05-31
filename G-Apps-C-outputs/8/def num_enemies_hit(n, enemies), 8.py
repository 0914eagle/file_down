
import math

def num_enemies_hit(n, enemies):
    max_enemies = 0
    
    for i in range(n):
        angles = []
        for j in range(n):
            if i != j:
                dx = enemies[j][0] - enemies[i][0]
                dy = enemies[j][1] - enemies[i][1]
                dist = math.sqrt(dx**2 + dy**2)
                if dist < enemies[i][2] + enemies[j][2]:
                    continue
                
                angle = math.atan2(dy, dx)
                delta = math.acos((enemies[i][2]**2 - enemies[j][2]**2 + dist**2) / (2 * enemies[i][2] * dist))
                
                angles.append((angle - delta, 1))
                angles.append((angle + delta, -1))
        
        angles.sort()
        count = 0
        for _, val in angles:
            count += val
            max_enemies = max(max_enemies, count)
    
    return max_enemies

# Read input
n = int(input())
enemies = []
for _ in range(n):
    x, y, r = map(float, input().split())
    enemies.append((x, y, r))

# Call the function and output the result
print(num_enemies_hit(n, enemies))
