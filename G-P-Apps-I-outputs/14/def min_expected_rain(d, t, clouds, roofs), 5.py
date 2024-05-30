
def min_expected_rain(d, t, clouds, roofs):
    def expected_rain_on_segment(start, end, clouds):
        total_rain = 0
        for cloud in clouds:
            if cloud[0] <= end and cloud[1] >= start:
                overlap_start = max(start, cloud[0])
                overlap_end = min(end, cloud[1])
                overlap_length = overlap_end - overlap_start
                total_rain += overlap_length * cloud[2] * cloud[3]
        return total_rain

    dp = [float('inf')] * (t+1)
    dp[0] = 0

    for i in range(1, t+1):
        for j in range(i):
            segment_rain = expected_rain_on_segment(j, i, clouds)
            dp[i] = min(dp[i], dp[j] + segment_rain)

    for roof in roofs:
        roof_rain = expected_rain_on_segment(roof[0], roof[1], clouds)
        dp[roof[1]] = min(dp[roof[1]], dp[roof[0]] + roof_rain)

    return dp[t]

# Reading input
d, t, c, r = map(int, input().split())
clouds = []
for _ in range(c):
    s, e, p, a = map(float, input().split())
    clouds.append((int(s), int(e), p, int(a))
roofs = [tuple(map(int, input().split())) for _ in range(r)]

# Calculating and printing the result
result = min_expected_rain(d, t, clouds, roofs)
print(round(result, 5))
```
