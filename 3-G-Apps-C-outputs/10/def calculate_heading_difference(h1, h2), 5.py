
import math

def calculate_heading_difference(h1, h2):
    diff = abs(h1 - h2)
    return min(diff, 360000 - diff)

def find_transportation_switching_scheme(t, n, transportation_types, points):
    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(1, n):
        for j in range(i):
            for k in range(t):
                d_min, a = transportation_types[k]
                total_distance = sum([points[m][0] for m in range(j, i)])
                total_heading_difference = sum([calculate_heading_difference(points[m][1], points[m+1][1]) for m in range(j, i-1)])
                
                if total_distance >= d_min and total_heading_difference <= a:
                    dp[i] = min(dp[i], dp[j] + 1)

    if dp[n-1] == float('inf'):
        return "IMPOSSIBLE"
    else:
        return dp[n-1]

# Input parsing
t, n = map(int, input().split())
transportation_types = []
for _ in range(t):
    d_min, a = map(int, input().split())
    transportation_types.append((d_min, a))

points = []
for _ in range(n-1):
    d, h = map(int, input().split())
    points.append((d, h))

# Call the function and print the result
result = find_transportation_switching_scheme(t, n, transportation_types, points)
print(result)
