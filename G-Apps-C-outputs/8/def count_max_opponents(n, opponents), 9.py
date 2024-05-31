
import math

def count_max_opponents(n, opponents):
    max_opponents = 0
    
    for i in range(n):
        angles = []
        for j in range(n):
            if i != j:
                dx = opponents[j][0] - opponents[i][0]
                dy = opponents[j][1] - opponents[i][1]
                distance = math.sqrt(dx*dx + dy*dy)
                if distance <= opponents[i][2] + opponents[j][2]:
                    angle = math.atan2(dy, dx)
                    angles.append(angle)
        angles.sort()
        
        k = len(angles)
        if k == 0:
            max_opponents = max(max_opponents, 1)
        for j in range(k):
            angle = angles[j] + 2*math.pi
            index = j
            while index < k and angles[index] <= angle:
                index += 1
            max_opponents = max(max_opponents, index - j + 1)
    
    return max_opponents

# Input
n = int(input())
opponents = []
for _ in range(n):
    x, y, r = map(float, input().split())
    opponents.append((x, y, r))

# Output
result = count_max_opponents(n, opponents)
print(result)
