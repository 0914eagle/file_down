
import math

def calculate_heading_change(h1, h2):
    return abs(h1 - h2)

def can_travel_between_points(d_min, a_max, d, h1, h2):
    if d < d_min:
        return False
    if calculate_heading_change(h1, h2) > a_max:
        return False
    return True

def find_transportation_switching_scheme(t, n, transportation_types, points):
    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(1, n):
        for j in range(i):
            for k in range(t):
                d_min, a_max = transportation_types[k]
                if can_travel_between_points(d_min, a_max, points[i][0], points[j][0], points[i][1]):
                    dp[i] = min(dp[i], dp[j] + 1)

    if dp[n-1] == float('inf'):
        return "IMPOSSIBLE"
    else:
        return dp[n-1]

# Input parsing
t, n = map(int, input().split())
transportation_types = []
for _ in range(t):
    d_min, a_max = map(int, input().split())
    transportation_types.append((d_min, a_max))

points = []
for _ in range(n-1):
    d, h = map(int, input().split())
    points.append((d, h))

# Find transportation switching scheme
result = find_transportation_switching_scheme(t, n, transportation_types, points)
print(result)
