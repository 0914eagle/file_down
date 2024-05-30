
import math

def calculate_distance(A, B, H, M):
    hour_angle = 30 * H + 0.5 * M
    minute_angle = 6 * M

    angle_difference = abs(hour_angle - minute_angle)
    if angle_difference > 180:
        angle_difference = 360 - angle_difference

    distance = math.sqrt(A**2 + B**2 - 2 * A * B * math.cos(math.radians(angle_difference)))
    return distance

A, B, H, M = map(int, input().split())
result = calculate_distance(A, B, H, M)
print("{:.20f}".format(result))
```
