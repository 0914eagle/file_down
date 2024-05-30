
import math

def calculate_distance(A, B, H, M):
    angle_hour = 30 * (H + M / 60)
    angle_minute = 6 * M
    x_hour = A * math.cos(math.radians(angle_hour))
    y_hour = A * math.sin(math.radians(angle_hour))
    x_minute = B * math.cos(math.radians(angle_minute))
    y_minute = B * math.sin(math.radians(angle_minute))

    distance = math.sqrt((x_hour - x_minute)**2 + (y_hour - y_minute)**2)
    return distance

A, B, H, M = map(int, input().split())
result = calculate_distance(A, B, H, M)
print(result)
```
