
import math

def expected_rain(d, t, c, r, clouds, roofs):
    def expected_rain_recursive(dist, time_left):
        if time_left <= 0:
            return 0

        min_rain = float('inf')
        for i in range(c):
            s, e, p, a = clouds[i]
            if s <= time_left <= e:
                prob = p * (e - time_left) / (e - s)
                rain = a * prob + expected_rain_recursive(dist, s)
                min_rain = min(min_rain, rain)

        for x, y in roofs:
            if dist <= x <= dist + time_left:
                min_rain = min(min_rain, expected_rain_recursive(y, time_left - (y - x)))

        return min_rain

    return expected_rain_recursive(0, t - d)

# Input parsing
d, t, c, r = map(int, input().split())
clouds = []
for _ in range(c):
    s, e, p, a = map(float, input().split())
    clouds.append((int(s), int(e), p, int(a))
roofs = [tuple(map(int, input().split())) for _ in range(r)]

# Calculate and print the minimum amount of expected rain
print(round(expected_rain(d, t, c, r, clouds, roofs), 5))
```
