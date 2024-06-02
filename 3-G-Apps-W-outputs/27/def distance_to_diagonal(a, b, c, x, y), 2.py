
import math

def distance_to_diagonal(a, b, c, x, y):
    return abs(a*x + b*y + c) / math.sqrt(a**2 + b**2)

def min_travel_distance(a, b, c, x1, y1, x2, y2):
    dist_to_diagonal_A = distance_to_diagonal(a, b, c, x1, y1)
    dist_to_diagonal_B = distance_to_diagonal(a, b, c, x2, y2)
    
    if (a*x1 + b*y1 + c) * (a*x2 + b*y2 + c) < 0:
        return dist_to_diagonal_A + dist_to_diagonal_B
    else:
        return abs(x1 - x2) + abs(y1 - y2)

a, b, c = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())

result = min_travel_distance(a, b, c, x1, y1, x2, y2)
print("{:.10f}".format(result))
