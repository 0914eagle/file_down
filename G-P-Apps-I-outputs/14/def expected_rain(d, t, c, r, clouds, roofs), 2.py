
import itertools

def expected_rain(d, t, c, r, clouds, roofs):
    def get_probabilities(clouds, t):
        probabilities = []
        for cloud in clouds:
            s, e, p, a = cloud
            if s < t and e > t:
                probabilities.append((p, a))
        return probabilities

    def generate_possible_paths(roofs, d):
        possible_paths = []
        for roof in roofs:
            x, y = roof
            possible_paths.append((0, x))
            possible_paths.append((y, d))
        return possible_paths

    def calculate_expected_rain(clouds, probabilities, paths):
        total_expected_rain = 0
        for path in paths:
            path_rain = 0
            for prob, rain in probabilities:
                path_rain += prob * rain * (path[1] - path[0])
            total_expected_rain += path_rain
        return total_expected_rain

    probabilities = get_probabilities(clouds, t)
    paths = generate_possible_paths(roofs, d)
    min_expected_rain = calculate_expected_rain(clouds, probabilities, paths)
    return min_expected_rain

# Parse input
d, t, c, r = map(int, input().split())
clouds = [list(map(float, input().split())) for _ in range(c)]
roofs = [tuple(map(int, input().split())) for _ in range(r)]

# Calculate and output the result
result = expected_rain(d, t, c, r, clouds, roofs)
print("{:.5f}".format(result))
```
