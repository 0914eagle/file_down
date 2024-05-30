
import itertools

def expected_rain(d, t, c, r, clouds, roofs):
    def calculate_expected_rain(time_remaining, position, rain_so_far):
        if time_remaining <= 0:
            return rain_so_far
        possible_rain = []
        for cloud in clouds:
            start_time, end_time, probability, rain_intensity = cloud
            if start_time <= time_remaining <= end_time:
                expected_rain_if_cloud = probability * rain_intensity
                new_position = position + (time_remaining * 1)
                for roof in roofs:
                    if position < roof[0] < new_position:
                        new_position = roof[0]
                        break
                possible_rain.append(expected_rain_if_cloud + calculate_expected_rain(end_time - start_time, new_position, rain_so_far))
        if not possible_rain:
            return rain_so_far
        return min(possible_rain)

    clouds = [list(map(float, line.split())) for line in clouds]
    roofs = [list(map(int, line.split())) for line in roofs]

    return calculate_expected_rain(t, 0, 0.0)

# Input parsing
input_line = input().strip().split()
d, t, c, r = map(int, input_line[:4])
clouds = input_line[4:4+c]
roofs = input_line[4+c:]

# Output
print(expected_rain(d, t, c, r, clouds, roofs))
```
