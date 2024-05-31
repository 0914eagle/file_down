
import math

def count_maximum_opponents(n, opponents):
    if n == 0:
        return 0

    angles = []
    for opponent in opponents:
        x, y, r = opponent
        dist = math.sqrt(x**2 + y**2)
        if dist <= r:
            angles.append((0, 1))
            angles.append((2*math.pi, -1))
        else:
            alpha = math.atan2(y, x)
            beta = math.acos(r / dist)
            start_angle = alpha - beta
            end_angle = alpha + beta
            angles.append((start_angle, 1))
            angles.append((end_angle, -1))

    angles.sort()
    max_opponents = 0
    curr_opponents = 0
    for angle in angles:
        curr_opponents += angle[1]
        max_opponents = max(max_opponents, curr_opponents)

    return max_opponents

# Reading input
n = int(input())
opponents = []
for _ in range(n):
    x, y, r = map(float, input().split())
    opponents.append((x, y, r))

# Call the function and print the result
result = count_maximum_opponents(n, opponents)
print(result)
