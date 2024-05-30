
import math

# Function to calculate the distance between the unfixed endpoints of the hands
def calculate_distance(A, B, H, M):
    hour_angle = (30 * H) + (0.5 * M)  # Angle covered by the hour hand
    minute_angle = 6 * M  # Angle covered by the minute hand

    x1 = A * math.cos(math.radians(hour_angle))  # x-coordinate of hour hand endpoint
    y1 = A * math.sin(math.radians(hour_angle))  # y-coordinate of hour hand endpoint

    x2 = B * math.cos(math.radians(minute_angle))  # x-coordinate of minute hand endpoint
    y2 = B * math.sin(math.radians(minute_angle))  # y-coordinate of minute hand endpoint

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  # Calculate distance between endpoints
    return distance

# Reading input values
A, B, H, M = map(int, input().split())

# Calculating and printing the distance between the unfixed endpoints
result = calculate_distance(A, B, H, M)
print("{:.20f}".format(result))
```
