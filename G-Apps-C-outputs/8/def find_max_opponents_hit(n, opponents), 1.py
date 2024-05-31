
import math

def find_max_opponents_hit(n, opponents):
    max_opponents = 0
    for i in range(n):
        angles = []
        for j in range(n):
            if j != i:
                dx = opponents[j][0] - opponents[i][0]
                dy = opponents[j][1] - opponents[i][1]
                dist = math.sqrt(dx**2 + dy**2)
                if dist <= opponents[i][2] + opponents[j][2]:
                    angle1 = math.atan2(opponents[j][1], opponents[j][0])
                    angle2 = math.atan2(opponents[j][1] - dy, opponents[j][0] - dx)
                    angles.append((angle1, 1))
                    angles.append((angle2, -1))
        
        angles.sort()
        
        opponents_hit = 0
        current_opponents = 0
        for angle in angles:
            current_opponents += angle[1]
            opponents_hit = max(opponents_hit, current_opponents)
        
        max_opponents = max(max_opponents, opponents_hit)
    
    return max_opponents

# Read input
n = int(input())
opponents = []
for _ in range(n):
    x, y, r = map(float, input().split())
    opponents.append((x, y, r))

# Call function and print output
print(find_max_opponents_hit(n, opponents))
