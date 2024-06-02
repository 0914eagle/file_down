
import math

def distance_to_diagonal(a, b, c, x, y):
    return abs(a*x + b*y + c) / math.sqrt(a**2 + b**2)

def min_travel_distance(a, b, c, x1, y1, x2, y2):
    dist_A_to_diagonal = distance_to_diagonal(a, b, c, x1, y1)
    dist_B_to_diagonal = distance_to_diagonal(a, b, c, x2, y2)
    
    dist_straight = abs(x2 - x1) + abs(y2 - y1)
    dist_diagonal = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    if (a*x1 + b*y1 + c) * (a*x2 + b*y2 + c) < 0:
        return dist_diagonal
    else:
        return min(dist_straight, dist_A_to_diagonal + dist_B_to_diagonal)

a, b, c = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())

result = min_travel_distance(a, b, c, x1, y1, x2, y2)
print("{:.10f}".format(result))
