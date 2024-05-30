
import math

def calculate_clock_distance(A, B, H, M):
    hour_angle = (H % 12 + M/60) * 30
    minute_angle = M * 6
    
    angle_diff = abs(hour_angle - minute_angle)
    if angle_diff > 180:
        angle_diff = 360 - angle_diff
    
    distance = math.sqrt(A**2 + B**2 - 2*A*B*math.cos(math.radians(angle_diff)))
    return distance

A, B, H, M = map(int, input().split())
result = calculate_clock_distance(A, B, H, M)
print(result)
```
