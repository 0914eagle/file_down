
import itertools

def expected_rain(d, t, c, r, clouds, roofs):
    def prob_no_rain(t):
        prob = 1
        for cloud in clouds:
            if cloud[0] <= t < cloud[1]:
                prob *= 1 - cloud[2]
        return prob

    def expected_rain_at_t(t):
        total_rain = 0
        for cloud in clouds:
            if cloud[0] <= t < cloud[1]:
                total_rain += cloud[2] * cloud[3] * prob_no_rain(t)
        return total_rain

    min_rain = float('inf')
    for i in range(d, t+1):
        rain_in_roofs = sum(abs(r[1] - r[0]) for r in roofs if r[0] <= i <= r[1])
        rain_outside_roofs = expected_rain_at_t(i) * (t - i)
        total_rain = rain_in_roofs + rain_outside_roofs
        min_rain = min(min_rain, total_rain)
    
    return round(min_rain, 5)

# Sample Input 1
d, t, c, r = 20, 60, 2, 1
clouds = [(5, 15, 0.33333, 30), (22, 60, 0.66666, 70)]
roofs = [(0, 10)]
print(expected_rain(d, t, c, r, clouds, roofs))  # Output: 466.662

# Sample Input 2
d, t, c, r = 3, 4, 2, 1
clouds = [(1, 3, 0.25, 8), (2, 4, 0.66667, 15)]
roofs = [(1, 2)]
print(expected_rain(d, t, c, r, clouds, roofs))  # Output: 10.00005

# Sample Input 3
d, t, c, r = 3, 4, 1, 0
clouds = [(0, 2, 0.25, 8)]
roofs = []
print(expected_rain(d, t, c, r, clouds, roofs))  # Output: 2.0
```
