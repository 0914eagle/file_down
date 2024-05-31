
import math

def max_opponents_hit(n, opponents):
    max_opponents = 0
    
    for i in range(n):
        angles = []
        
        for j in range(n):
            if i != j:
                dx = opponents[j][0] - opponents[i][0]
                dy = opponents[j][1] - opponents[i][1]
                dist = math.sqrt(dx**2 + dy**2)
                angle1 = math.atan2(dy, dx)
                
                if dist <= opponents[i][2] or dist <= opponents[j][2]:
                    angle2 = math.acos((opponents[i][2]**2 + dist**2 - opponents[j][2]**2) / (2 * opponents[i][2] * dist))
                    angles.append((angle1 - angle2, 1))
                    angles.append((angle1 + angle2, -1))
                else:
                    angle2 = math.acos((opponents[j][2]**2 + dist**2 - opponents[i][2]**2) / (2 * opponents[j][2] * dist))
                    angles.append((angle1 - angle2, 1))
                    angles.append((angle1 + angle2, -1))
        
        angles.sort()
        opponents_count = 0
        max_count = 0
        
        for angle in angles:
            opponents_count += angle[1]
            max_count = max(max_count, opponents_count)
        
        max_opponents = max(max_opponents, max_count)
    
    return max_opponents

# Read input
n = int(input())
opponents = []

for _ in range(n):
    x, y, r = map(float, input().split())
    opponents.append((x, y, r))

# Call the function
result = max_opponents_hit(n, opponents)

# Print the result
print(result)
