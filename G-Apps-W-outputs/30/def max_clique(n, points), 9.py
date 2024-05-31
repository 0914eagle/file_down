
def max_clique(n, points):
    points.sort()
    dp = [1] * n
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            xi, wi = points[i]
            xj, wj = points[j]
            if abs(xi - xj) >= wi + wj:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Input
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Output
print(max_clique(n, points))
