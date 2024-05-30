
import itertools

def expected_rain(d, t, c, r, clouds, roofs):
    def get_probability(cloud, time):
        if time >= cloud[0] and time < cloud[1]:
            return cloud[2]
        return 0

    def get_rain(cloud, time):
        if time >= cloud[0] and time < cloud[1]:
            return cloud[3]
        return 0

    def get_total_rain(probabilities, rains):
        total_rain = 0
        for p, r in zip(probabilities, rains):
            total_rain += p * r
        return total_rain

    min_rain = float('inf')

    for i in range(t):
        probabilities = [get_probability(cloud, i) for cloud in clouds]
        rains = [get_rain(cloud, i) for cloud in clouds]

        for breaks in itertools.product([0, 1], repeat=r):
            roof_rain = 0
            total_time = 0

            for j in range(r):
                if breaks[j] == 1:
                    roof_length = roofs[j][1] - roofs[j][0]
                    roof_rain += roof_length
                    total_time += roof_length

            remaining_time = t - i - total_time
            if remaining_time < 0:
                continue

            total_rain = get_total_rain(probabilities, rains) * remaining_time + roof_rain
            min_rain = min(min_rain, total_rain)

    return round(min_rain, 5)

# Input parsing
d, t, c, r = map(int, input().split())
clouds = [list(map(float, input().split())) for _ in range(c)]
roofs = [list(map(int, input().split())) for _ in range(r)]

# Call the function with input values
result = expected_rain(d, t, c, r, clouds, roofs)
print(result)
```
