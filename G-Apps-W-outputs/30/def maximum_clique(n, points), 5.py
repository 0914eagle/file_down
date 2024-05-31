
def maximum_clique(n, points):
    points.sort()
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if abs(points[i][0] - points[j][0]) >= points[i][1] + points[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Input parsing
n = int(input())
points = []
for _ in range(n):
    x, w = map(int, input().split())
    points.append((x, w))

print(maximum_clique(n, points))
