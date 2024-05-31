
def find_max_clique(n, points):
    points.sort()  # Sort points based on the coordinates
    dp = [1] * n  # Initialize a dynamic programming array with all values set to 1
    
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if abs(points[i][0] - points[j][0]) >= points[i][1] + points[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Read input
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Call the function and print the output
print(find_max_clique(n, points))
