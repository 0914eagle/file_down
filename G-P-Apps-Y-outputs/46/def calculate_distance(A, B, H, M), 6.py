
import math

def calculate_distance(A, B, H, M):
    angle_hour = (60*H + M) / 720 * 2 * math.pi
    angle_minute = M / 60 * 2 * math.pi

    x_hour = A * math.cos(angle_hour)
    y_hour = A * math.sin(angle_hour)

    x_minute = B * math.cos(angle_minute)
    y_minute = B * math.sin(angle_minute)

    distance = math.sqrt((x_hour - x_minute)**2 + (y_hour - y_minute)**2)
    return distance

A, B, H, M = map(int, input().split())
result = calculate_distance(A, B, H, M)
print("{:.20f}".format(result))
```
