
import math

def calculate_distance_between_hands(A, B, H, M):
    angle_hour = (30 * H) + (0.5 * M)
    angle_minute = 6 * M

    angle = abs(angle_hour - angle_minute)
    if angle > 180:
        angle = 360 - angle

    distance = math.sqrt(A**2 + B**2 - 2 * A * B * math.cos(math.radians(angle)))
    return distance

A, B, H, M = map(int, input().split())
distance = calculate_distance_between_hands(A, B, H, M)
print(distance)
```
