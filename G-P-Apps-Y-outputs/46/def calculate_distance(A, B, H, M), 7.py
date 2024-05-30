
import math

def calculate_distance(A, B, H, M):
    hour_angle = (30 * H) + (0.5 * M)
    minute_angle = 6 * M
    angle = abs(hour_angle - minute_angle)
    
    distance = math.sqrt(A**2 + B**2 - 2*A*B*math.cos(math.radians(angle)))
    return distance

A, B, H, M = map(int, input().split())
result = calculate_distance(A, B, H, M)
print(f"{result:.20f}")
```
