
import math

def distance_to_diagonal(a, b, c, x, y):
    return abs(a*x + b*y + c) / math.sqrt(a**2 + b**2)

def min_travel_distance(a, b, c, x1, y1, x2, y2):
    if a == 0:
        return abs(x2 - x1) + abs(y2 - y1)
    elif b == 0:
        return abs(x2 - x1) + abs(y2 - y1)
    else:
        dist_to_diagonal_A = distance_to_diagonal(a, b, c, x1, y1)
        dist_to_diagonal_B = distance_to_diagonal(a, b, c, x2, y2)
        dist_A_to_B = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return min(dist_to_diagonal_A + dist_to_diagonal_B, dist_A_to_B)

# Input
a, b, c = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())

# Output
result = min_travel_distance(a, b, c, x1, y1, x2, y2)
print("{:.10f}".format(result))