
def maximum_clique(n, points):
    points.sort(key=lambda x: x[0])  # Sort points by x coordinate
    dp = [0] * n  # Initialize dynamic programming table
    dp[0] = 1  # Base case
    
    for i in range(1, n):
        dp[i] = 1  # Initialize dp[i] to 1
        for j in range(i):
            if abs(points[i][0] - points[j][0]) >= points[i][1] + points[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)  # Update dp[i]
    
    return max(dp)

# Input processing
n = int(input())
points = []
for _ in range(n):
    x, w = map(int, input().split())
    points.append((x, w))

# Call the function and output the result
print(maximum_clique(n, points))
