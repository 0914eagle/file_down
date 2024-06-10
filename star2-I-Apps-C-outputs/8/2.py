
import math
def solve(opponents):
    angles = []
    for x, y, r in opponents:
        d = math.sqrt(x*x + y*y)
        if d > r:
            theta = math.asin(r/d)
            angles.append(math.atan2(y, x) - theta)
            angles.append(math.atan2(y, x) + theta)
    angles.sort()
    max_count = 0
    count = 0
    for i in range(1, len(angles)):
        if angles[i] - angles[i-1] < 1e-9:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
    max_count = max(max_count, count)
    return max_count

n = int(input())
opponents = []
for _ in range(n):
    x, y, r = map(float, input().split())
    opponents.append((x, y, r))
print(solve(opponents))

