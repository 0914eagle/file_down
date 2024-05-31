
def maximum_clique(n, points):
    points.sort()  # Sort points based on coordinates
    
    dp = [1] * n  # Initialize dynamic programming array to store the maximum clique size ending at each point
    for i in range(1, n):
        for j in range(i):
            if abs(points[i][0] - points[j][0]) >= points[i][1] + points[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Read input
n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

# Call the function and print the output
print(maximum_clique(n, points))
