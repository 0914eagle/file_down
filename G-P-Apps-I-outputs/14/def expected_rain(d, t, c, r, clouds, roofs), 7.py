
import itertools

def expected_rain(d, t, c, r, clouds, roofs):
    def calculate_rain_probabilities(cloud):
        rain_probabilities = [0] * (t + 1)
        for i in range(cloud[0], cloud[1]):
            rain_probabilities[i] = cloud[2]
        return rain_probabilities

    def calculate_combined_rain_probabilities(clouds):
        combined_rain_probabilities = [1]
        for cloud in clouds:
            cloud_rain_probabilities = calculate_rain_probabilities(cloud)
            combined_rain_probabilities = [p * q for p, q in itertools.product(combined_rain_probabilities, cloud_rain_probabilities)]
        return combined_rain_probabilities

    total_rain = 0
    combined_rain_probabilities = calculate_combined_rain_probabilities(clouds)
    for i in range(t):
        total_rain += sum([p * a for p, a in zip(combined_rain_probabilities, [cloud[3] for cloud in clouds])])

    for roof in roofs:
        total_rain = min(total_rain, sum([a for i in range(roof[0], roof[1]) for cloud in clouds for a in calculate_rain_probabilities(cloud)]))

    return total_rain

# Input parsing
d, t, c, r = map(int, input().split())
clouds = [list(map(float, input().split())) for _ in range(c)]
roofs = [list(map(int, input().split())) for _ in range(r)]

# Calculate and output the expected minimum amount of rain
print("{:.5f}".format(expected_rain(d, t, c, r, clouds, roofs))
```

