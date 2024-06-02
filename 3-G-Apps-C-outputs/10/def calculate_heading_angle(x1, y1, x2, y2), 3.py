
import math

def calculate_heading_angle(x1, y1, x2, y2):
    angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
    return angle if angle >= 0 else angle + 360

def find_transportation_switching_scheme(t, n, transportation_types, points):
    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(1, n):
        for j in range(i):
            for k in range(t):
                d_min, a = transportation_types[k]
                total_distance = sum(points[m][0] for m in range(j, i))
                heading_range = max(calculate_heading_angle(points[j][0], points[j][1], points[i][0], points[i][1]) - calculate_heading_angle(points[j][0], points[j][1], points[j+1][0], points[j+1][1]), calculate_heading_angle(points[j][0], points[j][1], points[j+1][0], points[j+1][1]) - calculate_heading_angle(points[i][0], points[i][1], points[j+1][0], points[j+1][1]))
                
                if total_distance >= d_min and heading_range <= a:
                    dp[i] = min(dp[i], dp[j] + 1)

    if dp[n-1] == float('inf'):
        return "IMPOSSIBLE"
    else:
        return dp[n-1]

# Input parsing
t, n = map(int, input().split())
transportation_types = [list(map(int, input().split())) for _ in range(t)]
points = [list(map(int, input().split())) for _ in range(n-1)]

# Call the function and output the result
result = find_transportation_switching_scheme(t, n, transportation_types, points)
print(result)
