
def maximum_clique(n, points):
    points.sort()  # Sort points by coordinate

    dp = [1] * n  # Initialize dynamic programming array

    for i in range(1, n):
        for j in range(i):
            if abs(points[i][0] - points[j][0]) >= points[i][1] + points[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Read input
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Output
print(maximum_clique(n, points))
