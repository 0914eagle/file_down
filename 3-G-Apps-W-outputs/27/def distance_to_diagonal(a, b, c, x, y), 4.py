
import math

def distance_to_diagonal(a, b, c, x, y):
    return abs(a*x + b*y + c) / math.sqrt(a**2 + b**2)

def min_travel_distance(a, b, c, x1, y1, x2, y2):
    dist1 = abs(x1 - x2) + abs(y1 - y2)  # Manhattan distance
    dist2 = distance_to_diagonal(a, b, c, x1, y1) + distance_to_diagonal(a, b, c, x2, y2)
    dist3 = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)  # Euclidean distance
    return min(dist1, dist2, dist3)

# Input
a, b, c = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())

# Output
result = min_travel_distance(a, b, c, x1, y1, x2, y2)
print("{:.10f}".format(result))
