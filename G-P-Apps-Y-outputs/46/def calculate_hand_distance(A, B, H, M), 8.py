
import math

def calculate_hand_distance(A, B, H, M):
    angle_h = 30 * H + 0.5 * M
    angle_m = 6 * M

    angle_diff = abs(angle_h - angle_m)
    if angle_diff > 180:
        angle_diff = 360 - angle_diff

    radian_angle = math.radians(angle_diff)
    
    distance = math.sqrt(A**2 + B**2 - 2 * A * B * math.cos(radian_angle))
    
    return distance

A, B, H, M = map(int, input().split())
result = calculate_hand_distance(A, B, H, M)
print('{:.20f}'.format(result))
```
