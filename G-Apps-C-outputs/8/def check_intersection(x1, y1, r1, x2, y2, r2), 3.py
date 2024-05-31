
import math

def check_intersection(x1, y1, r1, x2, y2, r2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if dist >= r1 + r2:
        return False
    if dist + min(r1, r2) < max(r1, r2):
        return False
    return True

def find_max_opponents(n, opponents):
    max_opponents = 0
    for i in range(n):
        count = 1
        for j in range(n):
            if i != j and check_intersection(opponents[i][0], opponents[i][1], opponents[i][2],
                                            opponents[j][0], opponents[j][1], opponents[j][2]):
                count += 1
        max_opponents = max(max_opponents, count)
    return max_opponents

# Input
n = int(input())
opponents = []
for _ in range(n):
    x, y, r = map(float, input().split())
    opponents.append((x, y, r))

# Find maximum opponents hit with one shot
max_opponents = find_max_opponents(n, opponents)
print(max_opponents)
