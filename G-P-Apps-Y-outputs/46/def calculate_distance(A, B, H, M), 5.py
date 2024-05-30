
import math

def calculate_distance(A, B, H, M):
    # Calculate the angles of the hour and minute hands at the given time
    angle_hour = (H % 12 + M / 60) * 30
    angle_minute = M * 6

    # Calculate the coordinates of the endpoints of the hour and minute hands
    x_hour = A * math.cos(math.radians(angle_hour))
    y_hour = A * math.sin(math.radians(angle_hour))
    x_minute = B * math.cos(math.radians(angle_minute))
    y_minute = B * math.sin(math.radians(angle_minute))

    # Calculate the distance between the endpoints
    distance = math.sqrt((x_hour - x_minute)**2 + (y_hour - y_minute)**2)
    
    return distance

# Read input values
A, B, H, M = map(int, input().split())

# Calculate and print the distance between the endpoints of the hands
print(calculate_distance(A, B, H, M))
```
