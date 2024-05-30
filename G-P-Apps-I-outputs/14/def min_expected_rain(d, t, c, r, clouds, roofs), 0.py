
def min_expected_rain(d, t, c, r, clouds, roofs):
    def calculate_expected_rain(curr_time, curr_pos):
        if curr_time >= t:
            return 0
        
        min_rain = float('inf')
        for cloud in clouds:
            if cloud[0] <= curr_time < cloud[1]:
                prob = cloud[2]
                rain = cloud[3]
                expected_rain = prob * rain + (1 - prob) * calculate_expected_rain(curr_time + 1, curr_pos)
                min_rain = min(min_rain, expected_rain)
        
        for roof in roofs:
            if curr_pos >= roof[0] and curr_pos < roof[1]:
                min_rain = min(min_rain, calculate_expected_rain(curr_time, roof[1]))
        
        if curr_pos < d:
            min_rain = min(min_rain, calculate_expected_rain(curr_time + 1, curr_pos + 1))
        
        return min_rain
    
    return calculate_expected_rain(0, 0)

# Input
d, t, c, r = map(int, input().split())
clouds = []
for _ in range(c):
    s, e, p, a = map(float, input().split())
    clouds.append((int(s), int(e), p, int(a)))
roofs = [tuple(map(int, input().split())) for _ in range(r)]

# Output
print("{:.5f}".format(min_expected_rain(d, t, c, r, clouds, roofs))
```
