
import math

def distance_to_diagonal(a, b, c, x, y):
    return abs(a*x + b*y + c) / math.sqrt(a**2 + b**2)

def min_travel_distance(a, b, c, x1, y1, x2, y2):
    if a == 0:
        return abs(x2 - x1) + abs(y2 - y1)
    elif b == 0:
        return abs(x2 - x1) + abs(y2 - y1)
    else:
        dist_A = distance_to_diagonal(a, b, c, x1, y1)
        dist_B = distance_to_diagonal(a, b, c, x2, y2)
        return dist_A + dist_B + math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Input
a, b, c = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())

# Output
print("{:.10f}".format(min_travel_distance(a, b, c, x1, y1, x2, y2)))
