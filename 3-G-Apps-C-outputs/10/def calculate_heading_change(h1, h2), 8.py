
import math

def calculate_heading_change(h1, h2):
    return min(abs(h1 - h2), 360000 - abs(h1 - h2))

def find_transportation_switching_scheme(t, n, transportation_types, points):
    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(1, n):
        for j in range(i):
            for k in range(t):
                d_min, a = transportation_types[k]
                total_distance = sum(points[m][0] for m in range(j, i))
                total_heading_change = sum(calculate_heading_change(points[m][1], points[m+1][1]) for m in range(j, i))

                if total_distance >= d_min and total_heading_change <= a:
                    dp[i] = min(dp[i], dp[j] + 1)

    return dp[n-1] if dp[n-1] != float('inf') else "IMPOSSIBLE"

# Input parsing
t, n = map(int, input().split())
transportation_types = [list(map(int, input().split())) for _ in range(t)]
points = [list(map(int, input().split())) for _ in range(n-1)]

# Call the function and print the output
print(find_transportation_switching_scheme(t, n, transportation_types, points))
