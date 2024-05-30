
def min_expected_rain(d, t, c, r, cloud_info, roof_info):
    dp = [[0] * (t + 1) for _ in range(d + 1)]

    for i in range(1, d + 1):
        dp[i][0] = float('inf')

    for s, e, p, a in cloud_info:
        for i in range(d + 1):
            for j in range(t + 1):
                if dp[i][j] != float('inf'):
                    dp[i][j] += p * a

        for i in range(e, t + 1):
            for j in range(d + 1):
                dp[j][i] -= p * a

    for x, y in roof_info:
        for i in range(x, y):
            for j in range(t + 1):
                dp[i][j] = 0

    for i in range(1, d + 1):
        for j in range(1, t + 1):
            dp[i][j] += min(dp[i-1][j-1], dp[i][j-1])

    return round(dp[d][t], 5)

# Input parsing
d, t, c, r = map(int, input().split())
cloud_info = [list(map(float, input().split())) for _ in range(c)]
roof_info = [list(map(int, input().split())) for _ in range(r)]

# Call the function with the input data
result = min_expected_rain(d, t, c, r, cloud_info, roof_info)
print(result)
```
