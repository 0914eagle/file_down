
import itertools

def expected_rain(d, t, c, r, clouds, roofs):
    max_time = max(cloud[1] for cloud in clouds)
    dp = [float('inf') for _ in range(max_time + 1)]
    dp[0] = 0
    
    for i in range(1, max_time + 1):
        for cloud in clouds:
            start, end, prob, rain = cloud
            if i >= start and i <= end:
                dp[i] = min(dp[i], dp[i - 1] + prob * rain)
            else:
                dp[i] = min(dp[i], dp[i - 1])

    roof_values = [0] * (d + 1)
    for roof in roofs:
        start, end = roof
        for i in range(start, end):
            roof_values[i] = 1

    total_rain = 0
    for i in range(d):
        if roof_values[i] == 1:
            total_rain += dp[t - d + i]

    return total_rain

# Input parsing
d, t, c, r = map(int, input().split())
clouds = []
for _ in range(c):
    s, e, p, a = map(float, input().split())
    clouds.append((int(s), int(e), p, int(a))

roofs = []
for _ in range(r):
    x, y = map(int, input().split())
    roofs.append((x, y))

print('{:.5f}'.format(expected_rain(d, t, c, r, clouds, roofs)))
```
